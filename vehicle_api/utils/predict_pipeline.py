
import pandas as pd
from utils.input_data_validation import load_object
import os
import datetime
import logging

#predicting class
class PredictPipeline:
    def __init__(self,modelpath:str):
        self.model_location=modelpath
        

    def predict(self, features):
        try:
            model_path = os.path.join(self.model_location, "model.pkl")
            model = None
            try:
                model = load_object(file_path=model_path)
                logging.info("Successfully loaded the model")
            except Exception as e:
                logging.info(f"Error loading the model: {e}")               
                return [0] 
            if model is None:
                logging.info("Model is None after loading")
                return [0]  

            prediction = model.predict(features)
            logging.info(f"prediction {prediction}")
            return prediction

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
        milage: str,
        engine_capacity:str,
        fuel:str,
        transmission: str
        ):

        self.mileage = milage

        self.yom = yom

        self.curr_year=datetime.datetime.now().year

        self.age=self.curr_year - int(self.yom) if int(self.yom) else 0

        self.model = model

        self.engine_capacity = engine_capacity

        self.fuel=fuel

        self.transmission=transmission


    def get_data_as_data_frame(self):
        try:

            custom_data_input_dict = {
                "Age": [self.age],
                "Mileage": [int(self.mileage)],
                "Engine Capacity": [self.engine_capacity],
                "Model": [self.model],
                "Fuel Type": [self.fuel],
                "Transmission": [self.transmission]        
            }

            return pd.DataFrame(custom_data_input_dict)

        
        except Exception as e:
            logging.error(f"An error occurred creating dataframe: {str(e)}")
            return None

