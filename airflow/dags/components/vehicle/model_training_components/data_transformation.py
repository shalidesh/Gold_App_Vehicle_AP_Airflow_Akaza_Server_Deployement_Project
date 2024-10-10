from components.utils.configs import host, database, port, user, password
import os
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from components.utils.utils import save_object

preprocessor_obj_file_path=os.path.join('artifacts',"vehicle","preprocessor.pkl")


def transform_data():
    try:
        numerical_columns = ["year_of_manufacture","engine_capacity"]
        categorical_columns = [
            "model",
            "transmission",
            "fuel_type"
        
        ]

        num_pipeline= Pipeline(
            steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("scaler",StandardScaler())

            ]
        )

        cat_pipeline=Pipeline(

            steps=[
            ("imputer",SimpleImputer(strategy="most_frequent")),
            ("one_hot_encoder",OneHotEncoder()),
            ("scaler",StandardScaler(with_mean=False))
            ]
        )

        preprocessor=ColumnTransformer(
            [
            ("num_pipeline",num_pipeline,numerical_columns),
            ("cat_pipelines",cat_pipeline,categorical_columns)
            ]
        )

        save_object(
                file_path=preprocessor_obj_file_path,
                obj=preprocessor
            )


    except Exception as e:
        raise print("errror",e)

  

    



    