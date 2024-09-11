import os
import pandas as pd
from constants.dataframes import honda_name_mapping,suzuki_name_mapping,toyota_name_mapping,nisaan_name_mapping,micro_name_mapping,mitsubishi_name_mapping
from utils.select_close_year import estimate_price


suzuki_model_path=os.path.join('models',"suzuki")
toyota_model_path=os.path.join('models',"toyota")
nissan_model_path=os.path.join('models',"nissan")
honda_model_path=os.path.join('models',"honda")
micro_model_path=os.path.join('models',"micro")
mitsubishi_model_path=os.path.join('models',"mitsubishi")

def price_calculate(df,manufacture,model,fuel,transmission,yom,engine_capacity):

    try:
        if manufacture=='NISSAN':
            cdb_model=nisaan_name_mapping.get(model)
            model_path=nissan_model_path
        elif manufacture=='SUZUKI':
            cdb_model=suzuki_name_mapping.get(model)
            model_path=suzuki_model_path
        elif manufacture=='MARUTI':
            cdb_model=suzuki_name_mapping.get(model)
            model_path=suzuki_model_path
        elif manufacture=='HONDA':
            cdb_model=honda_name_mapping.get(model)
            model_path=honda_model_path
        elif manufacture=='TOYOTA':
            cdb_model=toyota_name_mapping.get(model)
            model_path=toyota_model_path
        elif manufacture=='MICRO':
            cdb_model=micro_name_mapping.get(model)
            model_path=micro_model_path
        elif manufacture=='MITSUBISHI':
            cdb_model=mitsubishi_name_mapping.get(model)
            model_path=mitsubishi_model_path
       
        average_price=estimate_price(df,model_path, cdb_model, fuel, transmission,yom,engine_capacity)
       
        return average_price
    
    except Exception as e:
       raise Exception(e)