from constants.input_data import Transmission_list,fuel_list,upload_dataset_column_list
from constants.dataframes import nissan_mapp,suzuki_mapp,toyota_mapp,honda_mapp,micro_mapp,mitsubishi_mapp
import re
import re
import random
import math
import datetime
import pickle
import pandas as pd


#model loading
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        print("error occured at model loading",e)

#check model valid or not
def submodelCheck(manufacture:str,model:str):
    if manufacture=="NISSAN":
        if model in nissan_mapp['model'].values.tolist():
            return True
        else:
            return False
         
    elif manufacture=="SUZUKI":
        if model in suzuki_mapp['model'].values.tolist():
            return True
        else:
            return False
            
    elif manufacture=="TOYOTA":
        if model in toyota_mapp['model'].values.tolist():
            return True
        else:
            return False
    elif manufacture=="HONDA":
        if model in honda_mapp['model'].values.tolist():
            return True
        else:
            return False    
        
    elif manufacture=="MARUTI":
        if model in suzuki_mapp['model'].values.tolist():
            return True
        else:
            return False
        
    elif manufacture=="MICRO":
        if model in micro_mapp['model'].values.tolist():
            return True
        else:
            return False
        
    elif manufacture=="MITSUBISHI":
        if model in mitsubishi_mapp['model'].values.tolist():
            return True
        else:
            return False
         
    else:
        return False
    
#check vehicle transmission type 
def TransitionCheck(transmission:str):

    if transmission in Transmission_list:
        return True
    else:
        return False

#check vehicle fual type 
def fuelTypeCheck(fuel:str):
    if fuel in fuel_list:
        return True
    else:
        return False
    
def changeCapacity(engine_capacity:str):
    try:
        match = re.search(r'\d+', engine_capacity)
        if match:
            engine_capacity = int(match.group())
            return engine_capacity
        else:
            return None  
    
    except Exception as e:
        raise Exception(e)
    
def changeFuelType(fuel:str):
    try:
        if fuel=='PETROL+ELECTRIC' or fuel=='PETROL + ELECTRIC': 
            return 'HYBRID'
        else:
            return fuel
    
    except Exception as e:
        raise Exception(e)


def checkInputs(request_data):

    model=request_data.get('model').upper().strip() 
    manufacture = request_data.get('manufacture').upper().strip() 
    fuel=request_data.get('fuel').upper().strip() 
    transmission=request_data.get('transmission').upper().strip() 
    yom=request_data.get('yom').strip() 
    engine_capacity=request_data.get('engine_capacity').upper().strip()
    engine_capacity= changeCapacity(engine_capacity)

    print(fuel)

    if yom  and model and manufacture and fuel and transmission and engine_capacity:
        if  submodelCheck(manufacture,model) and TransitionCheck(transmission) and  fuelTypeCheck(fuel):
            print("Input Data is ok")
            return True 
        else:
            print("Input Data is  not ok")
            return False       
    else:
        return False


def DatasetValidation(df:pd.DataFrame):
    missing_columns = [col for col in upload_dataset_column_list if col not in df.columns]

    if missing_columns:
        return False
    else:
        return True
 
# Function to generate random mileage within specified range based on age
def generate_mileage(age:int):

    # Define mileage ranges based on age
    if age >= 23:
        mileage_range = (300000,400000)
    elif age >= 22:
        mileage_range = (280000, 300000)
    elif age >= 21:
        mileage_range = (260000, 279999)
    elif age >= 20:
        mileage_range = (250000, 259999)
    elif age >= 19:
        mileage_range = (240000, 249999)
    elif age >= 18:
        mileage_range = (235000, 239999)
    elif age >= 17:
        mileage_range = (210000, 225000)
    elif age >= 16:
        mileage_range = (190000, 210000)
    elif age >= 15:
        mileage_range = (180000, 189000)
    elif age >= 14:
        mileage_range = (170000, 179999)
    elif age >= 13:
        mileage_range = (160000, 169999)
    elif age >= 12:
        mileage_range = (150000, 159999)
    elif age >= 11:
        mileage_range = (140000, 149999)
    elif age >= 10:
        mileage_range = (130000, 139999)
    elif age >= 9:
        mileage_range = (120000, 129999)
    elif age >= 8:
        mileage_range = (110000, 119999)
    elif age >= 7:
        mileage_range = (100000, 110000)
    elif age >= 6:
        mileage_range = (80000, 100000)
    elif age >= 5:
        mileage_range = (70000, 80000)
    elif age >= 4:
        mileage_range = (60000, 65000)
    elif age >= 3:
        mileage_range = (50000, 60000)
    elif age >= 2:
        mileage_range = (40000, 45000)
    elif age >= 1:
        mileage_range = (30000, 40000)
    
    # Calculate the exponential of 2
    Age_factor = 44801.64*(math.exp(0.0798*age))
    adjusted_mileage = int(random.randint(mileage_range[0], mileage_range[1])/ Age_factor + (random.randint(mileage_range[0], mileage_range[1])))
    
    return adjusted_mileage

# Define the function to generate adjusted mileage
def generate_adjusted_mileage(yom):

    curr_year=datetime.datetime.now().year
    age=curr_year - int(yom) if int(yom) else 0
    Mileage = generate_mileage(age)
    
    return Mileage
