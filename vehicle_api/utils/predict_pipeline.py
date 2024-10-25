
import pandas as pd
from utils.input_data_validation import load_object
import os
import logging

#predicting class
class PredictPipeline:
    def __init__(self,modelpath:str,preprocess_path:str):
        self.model_location=modelpath
        self.preprocessor_path=preprocess_path
       
    def predict(self,features):

        print(features.info())
        try:
            
            print("Before Loading")
            model=load_object(file_path=self.model_location)
            preprocessor=load_object(file_path=self.preprocessor_path)
            print("After Loading")

            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except FileNotFoundError:
            logging.error("Model or preprocessor file not found.")
            return [0] 
        except Exception as e:
            logging.error(f"An error occurred during prediction: {str(e)}")
            return [0]
        
class CustomDataAutoFinance:
    def __init__(self,
        yom: str,
        model:str,
        engine_capacity:str,
        fuel:str,
        transmission: str
        ):

        self.yom = yom
        self.model = model
        self.engine_capacity = engine_capacity
        self.fuel=fuel
        self.transmission=transmission


    def get_data_as_data_frame(self):
        try:

            custom_data_input_dict = {
                "year_of_manufacture": [self.yom],
                "engine_capacity": [self.engine_capacity],
                "model": [self.model],
                "fuel_type": [self.fuel],
                "transmission": [self.transmission]        
            }

            return pd.DataFrame(custom_data_input_dict)

        
        except Exception as e:
            logging.error(f"An error occurred creating dataframe: {str(e)}")
            return None
