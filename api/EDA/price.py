from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash
import os
from bson import json_util
import pandas as pd
import os
import nltk
nltk.download('punkt')
from flask_cors import CORS
import yfinance as yf
from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import json
from prophet.serialize import model_to_json, model_from_json

# Load model
with open('models/model_prophet.json', 'r') as fin:
    model = model_from_json(json.load(fin)) 

# When you want to load the models for prediction, read them from the files
with open('models/model_regressor1.json', 'r') as fin:
    model_regressor1 = model_from_json(json.load(fin))

with open('models/model_regressor2.json', 'r') as fin:
    model_regressor2 = model_from_json(json.load(fin))

with open('models/model_regressor3.json', 'r') as fin:
    model_regressor3 = model_from_json(json.load(fin))

with open('models/model_regressor4.json', 'r') as fin:
    model_regressor4 = model_from_json(json.load(fin))


import pandas as pd
from datetime import datetime, timedelta

# Define the date range for iteration
start_date = pd.to_datetime('2024-06-13')
end_date = pd.to_datetime('2024-10-01')
dataset_last_given_date = pd.to_datetime('2024-06-12')

# Initialize an empty DataFrame to store the results
all_forecasts = pd.DataFrame()

# Define the function ounce_lkr (assuming it's a custom function)
def ounce_lkr(value):
    return value * 0.035274  # Example conversion factor (adjust as needed)

# Loop through each day in the range
current_date = start_date
while current_date <= end_date:
    today_date =pd.to_datetime('today').normalize()
    request_date = current_date  # Assuming we are requesting for the same day

    day_count_difference_lastday_and_today = (today_date - dataset_last_given_date).days
    day_count_difference_requested_date_and_today = (request_date - today_date).days
    period = day_count_difference_lastday_and_today + day_count_difference_requested_date_and_today

    # Make future dataframe for regressors
    future_regressor = model.make_future_dataframe(periods=period)
    
    # Make predictions for each regressor
    forecast_regressor1 = model_regressor1.predict(future_regressor)
    forecast_regressor2 = model_regressor2.predict(future_regressor)
    forecast_regressor3 = model_regressor3.predict(future_regressor)
    forecast_regressor4 = model_regressor4.predict(future_regressor)

    # Prepare future dataframe for main model
    future = future_regressor.copy()
    future['regressor1'] = forecast_regressor1['yhat']
    future['regressor2'] = forecast_regressor2['yhat']
    future['regressor3'] = forecast_regressor3['yhat']
    future['regressor4'] = forecast_regressor4['yhat']

    forecast = model.predict(future)
    forecast = forecast[['ds', 'yhat', 'yhat_upper']]

    cols = [col for col in forecast.columns if col != 'ds']
    forecast[cols] = forecast[cols].applymap(ounce_lkr)

    forecast['yhat_manipulation'] = forecast['yhat_upper'] + 15000
    forecast['yhat_lower_manipulation'] = forecast['yhat_upper'] + 5000
    forecast['yhat_upper_manipulation'] = forecast['yhat_upper'] + 20000

    forecast['yhat_manipulation_smooth'] = forecast['yhat_manipulation'].rolling(window=7, min_periods=1).mean()
    forecast['yhat_lower_manipulation_smooth'] = forecast['yhat_lower_manipulation'].rolling(window=5, min_periods=1).mean()
    forecast['yhat_upper_manipulation_smooth'] = forecast['yhat_upper_manipulation'].rolling(window=5, min_periods=1).mean()

    response_dataframe = forecast[["ds", "yhat_manipulation_smooth", "yhat_lower_manipulation_smooth", "yhat_upper_manipulation_smooth"]]

    # Append the results to the all_forecasts DataFrame
    all_forecasts = pd.concat([all_forecasts, response_dataframe])

    # Move to the next day
    current_date += timedelta(days=1)

# Remove any duplicates and sort by date
all_forecasts = all_forecasts.drop_duplicates().sort_values(by='ds').reset_index(drop=True)

all_forecasts.to_csv("final_data.csv")
