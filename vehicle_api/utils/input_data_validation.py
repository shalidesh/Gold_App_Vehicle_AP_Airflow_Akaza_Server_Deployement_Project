from constants.input_data import Transmission_list,fuel_list
from constants.dataframes import nissan_mapp,suzuki_mapp,toyota_mapp,honda_mapp,micro_mapp,mitsubishi_mapp
import re
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


def checkInputs(model,manufacture,fuel,transmission,engine_capacity,yom):

    engine_capacity= changeCapacity(engine_capacity)

    if yom  and model and manufacture and fuel and transmission and engine_capacity:
        if  submodelCheck(manufacture,model) and TransitionCheck(transmission) and  fuelTypeCheck(fuel):
            print("Input Data is ok")
            return True 
        else:
            print("Input Data is  not ok")
            return False       
    else:
        return False

 