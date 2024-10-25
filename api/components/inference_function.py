import os
import pandas as pd
import numpy as np
from prophet import Prophet
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import joblib
from datetime import datetime
import logging
from components.datasets_paths import model_dir,dataset_dir


# Load the saved Prophet model
prophet_model = joblib.load(os.path.join(model_dir, "prophet_model.pkl"))
xgb_model = xgb.XGBRegressor()
xgb_model.load_model(os.path.join(model_dir, "xgb_model.json"))
scaler = joblib.load(os.path.join(model_dir, "scaler.pkl"))
regressors = joblib.load(os.path.join(model_dir, "regressors.pkl"))


# Function to apply lag feature creation on the residuals column
def prepare_data_with_lags(df):
    # Forecast the trend with Prophet
    df_forecast = prophet_model.predict(df[['ds'] + regressors])
    
    # Calculate residuals (actual - forecast)
    df['residuals'] = df['y'] - df_forecast['yhat']
    
    # Create lag features for the residuals
    df_with_lags = create_lag_features(df, lags=90, target_col='residuals')
    
    # Drop rows with NaN values caused by shifting (lags)
    df_with_lags.dropna(inplace=True)
    
    return df_with_lags

# Function to handle forecast
def forecast_up_to_date(selected_date):
    # Load the dataset
    df = pd.read_csv(dataset_dir)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df = df.rename(columns={'date': 'ds', 'gold_lkr': 'y'})

    # Prepare the data with lags
    df_with_lags = prepare_data_with_lags(df)
    
    # Convert the selected date to datetime
    selected_date = datetime.strptime(selected_date, "%Y-%m-%d")
    
    # Prophet forecast for future dates
    future_dates = pd.date_range(start=df['ds'].max(), end=selected_date, freq='B')
    future = pd.DataFrame(future_dates, columns=['ds'])
    
    # Use the last available regressor values for the future predictions
    last_regressor_values = df[regressors].iloc[-1].to_dict()
    for regressor in regressors:
        future[regressor] = last_regressor_values[regressor]

    # Prophet forecast for the selected future dates
    prophet_future_forecast = prophet_model.predict(future)
    
    # Create the last sequence of lag features (residuals) from the training data
    last_sequence = df_with_lags.iloc[-1][regressors + [f'lag_{i}' for i in range(1, 91)]].values
    
    # Predict residuals using XGBoost
    future_residuals_pred = make_future_residual_predictions(last_sequence, xgb_model, num_predictions=len(future_dates))

    # Combine Prophet's predictions with XGBoost's residuals without using abs()
    future_predictions = prophet_future_forecast['yhat'] + np.abs(future_residuals_pred)
    
    # Apply the final formula transformation ((future_predictions / 31.1035) * 8)
    final_predictions = (future_predictions / 31.1035) * 8

    # Return the forecasted values and the corresponding dates
    return pd.DataFrame({
        'Date': future_dates,
        'Prophet_Prediction': prophet_future_forecast['yhat'],
        'XGBoost_Residuals': future_residuals_pred,
        'Hybrid_Prediction': future_predictions,
        'yhat_manipulation_smooth': (final_predictions+8000).astype(int)
    })


# Function to create lag features for residuals
def create_lag_features(data, lags, target_col):
    for lag in range(1, lags + 1):
        data[f'lag_{lag}'] = data[target_col].shift(lag)
    return data


# Function to make future residual predictions using XGBoost
def make_future_residual_predictions(last_sequence, model, num_predictions=90):
    future_residuals = []
    current_seq = last_sequence
    
    for _ in range(num_predictions):
        # Ensure that the correct number of features (regressors + lags) are passed to the model
        if len(current_seq) != scaler.n_features_in_:
            logging.warning(f"Feature mismatch: Expected {scaler.n_features_in_}, but got {len(current_seq)}.")
            # If necessary, pad the sequence with zeros (or handle appropriately)
            current_seq = np.pad(current_seq, (0, scaler.n_features_in_ - len(current_seq)), 'constant')
        
        current_seq_scaled = scaler.transform([current_seq])
        future_pred_residual = model.predict(current_seq_scaled)
        
        # Append the predicted residuals
        future_residuals.append(future_pred_residual[0])
        
        # Shift the lag sequence and append the new residual
        current_seq = np.roll(current_seq, -1)
        current_seq[-1] = future_pred_residual

    return future_residuals