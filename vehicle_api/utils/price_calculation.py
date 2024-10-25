import os
from constants.dataframes import honda_name_mapping,suzuki_name_mapping,toyota_name_mapping,nisaan_name_mapping,micro_name_mapping,mitsubishi_name_mapping
from utils.select_close_year import estimate_price

suzuki_model_path=os.path.join('artifacts',"SUZUKI_model.pkl")
toyota_model_path=os.path.join('artifacts',"TOYOTA_model.pkl")
nissan_model_path=os.path.join('artifacts',"NISSAN_model.pkl")
honda_model_path=os.path.join('artifacts',"HONDA_model.pkl")
micro_model_path=os.path.join('artifacts',"MICRO_model.pkl")
mitsubishi_model_path=os.path.join('artifacts',"MITSUBISHI_model.pkl")

suzuki_preprocessor_path=os.path.join('artifacts',"SUZUKI_preprocessor.pkl")
toyota_preprocessor_path=os.path.join('artifacts',"TOYOTA_preprocessor.pkl")
nissan_preprocessor_path=os.path.join('artifacts',"NISSAN_preprocessor.pkl")
honda_preprocessor_path=os.path.join('artifacts',"HONDA_preprocessor.pkl")
micro_preprocessor_path=os.path.join('artifacts',"MICRO_preprocessor.pkl")
mitsubishi_preprocessor_path=os.path.join('artifacts',"MITSUBISHI_preprocessor.pkl")

def price_calculate(df,manufacture,model,fuel,transmission,yom,engine_capacity):

    try:
        if manufacture=='NISSAN':
            cdb_model=nisaan_name_mapping.get(model)
            model_path=nissan_model_path
            preprocessor_path=nissan_preprocessor_path
        elif manufacture=='SUZUKI':
            cdb_model=suzuki_name_mapping.get(model)
            model_path=suzuki_model_path
            preprocessor_path=suzuki_preprocessor_path
        elif manufacture=='MARUTI':
            cdb_model=suzuki_name_mapping.get(model)
            model_path=suzuki_model_path
            preprocessor_path=suzuki_preprocessor_path
        elif manufacture=='HONDA':
            cdb_model=honda_name_mapping.get(model)
            model_path=honda_model_path
            preprocessor_path=honda_preprocessor_path
        elif manufacture=='TOYOTA':
            cdb_model=toyota_name_mapping.get(model)
            model_path=toyota_model_path
            preprocessor_path=toyota_preprocessor_path
        elif manufacture=='MICRO':
            cdb_model=micro_name_mapping.get(model)
            model_path=micro_model_path
            preprocessor_path=micro_preprocessor_path
        elif manufacture=='MITSUBISHI':
            cdb_model=mitsubishi_name_mapping.get(model)
            model_path=mitsubishi_model_path
            preprocessor_path=mitsubishi_preprocessor_path

        print(cdb_model)
        print(model_path)
       
        average_price=estimate_price(df,model_path,preprocessor_path, cdb_model, fuel, transmission,yom,engine_capacity)
       
        return average_price
    
    except Exception as e:
       raise Exception(e)