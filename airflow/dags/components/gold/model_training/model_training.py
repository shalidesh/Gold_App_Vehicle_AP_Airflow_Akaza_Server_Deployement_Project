import psycopg2
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from tqdm import tqdm 
from components.utils.database_table_creation import create_table,check_table,populate_table,upload_table_gold
from components.utils.configs import host, database, port, user, password
import numpy as np
from prophet import Prophet
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import joblib

artifacts_path=os.path.join("artifacts","gold")

# Create lag features for the residuals for a 90-day sliding window
def create_lag_features(data, lags, target_col):
    for lag in range(1, lags + 1):
        data[f'lag_{lag}'] = data[target_col].shift(lag)
    return data


# Function to make future predictions of residuals using XGBoost
def make_future_residual_predictions(last_sequence, model, num_predictions=90):
    future_residuals = []
    current_seq = last_sequence
    
    for _ in range(num_predictions):
        future_pred_residual = model.predict(np.array([current_seq]))
        future_residuals.append(future_pred_residual[0])
        
        current_seq = np.roll(current_seq, -1)
        current_seq[-1] = future_pred_residual

    return future_residuals

def forecast_model_training(source_table):

    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:

            query = f"SELECT * FROM {source_table}"
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=column_names)

            columns_to_convert = ['gold_lkr', 'gold_price_usd', 'silver_price', 'sp_500_index', 'nyse_com_index', 'usd_selling_exrate', 'gold_futures', 'effr']
            df[columns_to_convert] = df[columns_to_convert].apply(lambda x: x.astype(float))

            df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
            df = df.rename(columns={'date': 'ds', 'gold_lkr': 'y'})

            # Prepare the regressor variables
            regressors = ['gold_price_usd', 'silver_price', 'sp_500_index', 'nyse_com_index', 'usd_selling_exrate', 'gold_futures', 'effr']

            # Initialize and fit the Prophet model to capture the trend and seasonality
            prophet_model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)

            # Add each independent variable as a regressor in Prophet
            for regressor in regressors:
                prophet_model.add_regressor(regressor)

            # Fit the Prophet model on the training data
            prophet_model.fit(df[['ds', 'y'] + regressors])

            # Make predictions using the Prophet model
            df_forecast = prophet_model.predict(df[['ds'] + regressors])

            # Calculate the residuals (actual - predicted by Prophet)
            df['residuals'] = df['y'] - df_forecast['yhat']

            # Create lag features for the residuals
            df = create_lag_features(df, lags=90, target_col='residuals')

            # Drop rows with NaN values caused by shifting (lags)
            df.dropna(inplace=True)

            # Prepare features (X) and target (y) for XGBoost (we are predicting the residuals)
            X = df.drop(columns=['ds', 'y', 'residuals'])
            y = df['residuals']

            # Split the data into training and testing sets (80% training, 20% testing)
            train_size = int(len(df) * 0.8)
            X_train, X_test = X[:train_size], X[train_size:]
            y_train, y_test = y[:train_size], y[train_size:]

            # Standardize the features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Hyperparameter tuning using GridSearchCV for XGBoost
            # param_grid = {
            #     'learning_rate': [0.0001, 0.001, 0.01],
            #     'max_depth': [10, 15, 20],
            #     'n_estimators': [500, 1000, 1500],
            #     'min_child_weight': [1, 5, 10],
            # }

            param_grid = {
                'learning_rate': [0.001],
                'max_depth': [10],
                'n_estimators': [500],
                'min_child_weight': [1],
            }

            xgb_model = xgb.XGBRegressor(objective='reg:squarederror')

            grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', verbose=1)
            grid_search.fit(X_train_scaled, y_train)

            # Best parameters from GridSearch
            print(f'Best parameters from GridSearchCV: {grid_search.best_params_}')

            # Use the best parameters to train the XGBoost model
            xgb_model = xgb.XGBRegressor(**grid_search.best_params_)
            xgb_model.fit(X_train_scaled, y_train)

            # Predict the residuals on the test set
            residuals_pred = xgb_model.predict(X_test_scaled)

            # Combine Prophet's predictions with XGBoost's predictions of the residuals
            prophet_forecast_test = prophet_model.predict(df[['ds'] + regressors].iloc[train_size:])
            prophet_test_predictions = prophet_forecast_test['yhat']

            # Final predictions are Prophet's predictions + XGBoost's predicted residuals
            final_predictions = prophet_test_predictions + residuals_pred

            # Calculate the RMSE to evaluate the combined model's performance
            actual_test_values = df['y'].iloc[train_size:]
            rmse = np.sqrt(mean_squared_error(actual_test_values, final_predictions))
            print(f'Root Mean Squared Error (RMSE) of the hybrid model: {rmse}')

            
            # Create a directory to save the model files
            os.makedirs(artifacts_path, exist_ok=True)

            # Save the Prophet model using joblib
            joblib.dump(prophet_model, os.path.join(artifacts_path, "prophet_model.pkl"))

            # Save the XGBoost model
            xgb_model.save_model(os.path.join(artifacts_path, "xgb_model.json"))

            # Save the StandardScaler
            joblib.dump(scaler, os.path.join(artifacts_path, "scaler.pkl"))

            # Save the regressor names
            joblib.dump(regressors, os.path.join(artifacts_path, "regressors.pkl"))

            print("All necessary files for prediction have been saved in the 'model_files' directory.")


    
