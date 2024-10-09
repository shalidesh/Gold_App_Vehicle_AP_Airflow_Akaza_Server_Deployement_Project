import psycopg2
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from components.utils.utils import load_object,evaluate_models,save_object
from components.utils.configs import host, database, port, user, password


preprocessor_path=os.path.join('artifacts',"vehicle","preprocessor.pkl")


def train_model(source_table1,train_model_name):

    trained_model_file_path=os.path.join("artifacts","vehicle",f"{train_model_name}_model.pkl")

    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:

            query = f"SELECT * FROM {source_table1}"
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            train_df = pd.DataFrame(rows, columns=column_names)
            train_df = train_df.groupby('brand').get_group(train_model_name)

            # train_set,test_set=train_test_split(train_df,test_size=0.1,random_state=42)
            train_set,test_set=train_df,train_df

            preprocessor=load_object(file_path=preprocessor_path)
      
            train_set['vehicle_price']=train_set['vehicle_price'].astype(int)
            train_set['engine_capacity']=train_set['engine_capacity'].astype(int)
            train_set['year_of_manufacture']=train_set['year_of_manufacture'].astype(int)
            train_set['model']=train_set['model'].str.upper()
            train_set['transmission']=train_set['transmission'].str.upper()
            train_set['fuel_type']=train_set['fuel_type'].str.upper()

            test_set['vehicle_price']=test_set['vehicle_price'].astype(int)
            test_set['engine_capacity']=test_set['engine_capacity'].astype(int)
            test_set['year_of_manufacture']=test_set['year_of_manufacture'].astype(int)
            test_set['transmission']=test_set['transmission'].str.upper()
            test_set['fuel_type']=test_set['fuel_type'].str.upper()


            target_column_name="vehicle_price"

            exclude_column_names=['vehicle_price','brand','posted_date']

            input_feature_train_df=train_set.drop(columns=exclude_column_names,axis=1)
            target_feature_train_df=train_set[target_column_name]

            input_feature_test_df=test_set.drop(columns=exclude_column_names,axis=1)
            target_feature_test_df=test_set[target_column_name]


            input_feature_train_arr=preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor.transform(input_feature_test_df)

            input_feature_train_arr_dense = input_feature_train_arr.toarray()
            train_arr = np.c_[input_feature_train_arr_dense, target_feature_train_df.values]

            input_feature_test_arr_dense = input_feature_test_arr.toarray()
            test_arr = np.c_[input_feature_test_arr_dense, target_feature_test_df.values]

            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            params={
                    "Decision Tree": {
                        'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                        # 'splitter':['best','random'],
                        # 'max_features':['sqrt','log2'],
                    },
                    "Random Forest":{
                        # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    
                        # 'max_features':['sqrt','log2',None],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "Gradient Boosting":{
                        # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                        'learning_rate':[.1,.01,.05,.001],
                        'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                        # 'criterion':['squared_error', 'friedman_mse'],
                        # 'max_features':['auto','sqrt','log2'],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "Linear Regression":{},
                    "XGBRegressor":{
                        'learning_rate':[.1,.01,.05,.001],
                        'n_estimators': [8,16,32,64,128,256]
                    },
                    "CatBoosting Regressor":{
                        'depth': [6,8,10],
                        'learning_rate': [0.01, 0.05, 0.1],
                        'iterations': [30, 50, 100]
                    },
                    "AdaBoost Regressor":{
                        'learning_rate':[.1,.01,0.5,.001],
                        # 'loss':['linear','square','exponential'],
                        'n_estimators': [8,16,32,64,128,256]
                    }
                    
                }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                            models=models,param=params)
            
            print(f'model report is {model_report}')

             ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]
            print(f"best model is :{best_model}")

            #Log the best hyperparameters for the best model
            best_hyperparams = params[best_model_name]
            for param, value in best_hyperparams.items():
                print(param, value)

            if best_model_score<0.6:
                print("No best model found")

            print(f"Best found model on both training and testing dataset")

            save_object(
                file_path=trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            print(f'r2_square is {r2_square}')

            
