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

def ounce_lkr(x):
    price = (x / 31.1035) * 8
    rounded_price = round(price / 100.0) * 100
    return rounded_price


date_string='2025-1-2'
request_date = pd.to_datetime(date_string)

today_date = pd.to_datetime('today').normalize()
dataset_last_given_date = pd.to_datetime('2024-09-27')

day_count_difference_lastday_and_today = (today_date - dataset_last_given_date).days
day_count_difference_requested_date_and_today = (request_date - today_date).days

period=day_count_difference_lastday_and_today+day_count_difference_requested_date_and_today

future_regressor = model.make_future_dataframe(periods=period)
print(future_regressor)
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

forecast=forecast[['ds','yhat','yhat_upper']]

cols = [col for col in forecast.columns if col != 'ds']

forecast[cols] = forecast[cols].applymap(ounce_lkr)

forecast['yhat_manipulation'] = forecast['yhat_upper']+22000
forecast['yhat_lower_manipulation']=forecast['yhat_upper']+13000
forecast['yhat_upper_manipulation']=forecast['yhat_upper']+25000

forecast['yhat_manipulation_smooth'] = forecast['yhat_manipulation'].rolling(window=7, min_periods=1).mean().round(-2)
forecast['yhat_lower_manipulation_smooth'] = forecast['yhat_lower_manipulation'].rolling(window=5, min_periods=1).mean().round(-2)
forecast['yhat_upper_manipulation_smooth'] = forecast['yhat_upper_manipulation'].rolling(window=5, min_periods=1).mean().round(-2)

response_dataframe=forecast[["ds","yhat_manipulation_smooth","yhat_lower_manipulation_smooth","yhat_upper_manipulation_smooth"]]

response_dataframe.to_csv('2024-10-2.csv')