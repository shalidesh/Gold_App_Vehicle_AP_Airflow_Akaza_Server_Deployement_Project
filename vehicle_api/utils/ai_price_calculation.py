import os
from utils.predict_pipeline import CustomDataAutoFinance,PredictPipeline

def round_nearest_50000(number):
    return round(number / 50000) * 50000

#calculate ai price
def calculate_ai_price(cdb_model,model_path,preprocessor_path, fuel, transmission, year,engine_capacity):

    data=CustomDataAutoFinance(
                    yom=year,
                    model=cdb_model,
                    engine_capacity=engine_capacity,
                    fuel=fuel,
                    transmission=transmission

                )
    pred_df=data.get_data_as_data_frame()                
    predict_pipeline=PredictPipeline(model_path,preprocessor_path) 
    results=predict_pipeline.predict(pred_df)

    round_price=round(float(results[0]),0)

    rounded_number=round_nearest_50000(round_price)
    print(f'ai estimated price- {rounded_number}')
    return rounded_number