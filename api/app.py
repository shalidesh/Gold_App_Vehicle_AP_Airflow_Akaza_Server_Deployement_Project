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
import numpy as np
import os
from prophet.serialize import model_to_json, model_from_json

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://mongo:27017/gold_data"
app.config["MONGO_URI"] = "mongodb://host.docker.internal:27017/gold_data";
CORS(app)

mongo = PyMongo(app)

news_df = os.path.join("airflow_scrape_database", "gold_post_data.csv")
train_df_path = os.path.join("local_databases", "gold_train_data.csv")
gold_df_path = os.path.join("local_databases", "gold_databases.csv")

train_df=pd.read_csv(train_df_path)
gold_df=pd.read_csv(gold_df_path)

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


@app.route('/api/gold_price', methods=['GET'])
def get_gold_price():
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
    
    link='https://www.kitco.com/'
    
    response = requests.get(link,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    header = soup.find("div", class_='flex justify-between gap-2')

    # Find all h3 tags within the header
    h3_tags = header.find_all("div",class_='text-right font-medium')
    span_tags = header.find_all("span")

    texts = [h3.text for h3 in h3_tags]
    spantexts = [h3.text for h3 in span_tags]
    bid, ask= texts
    change, performance = spantexts


    price_list={

        'bid':bid,
        'ask':ask,
        'change':change,
        'performance':performance
    }

    return jsonify(price_list)


@app.route('/api/auth/register', methods=['POST'])
def register():
    print("called register")
    _json = request.json
    _username = _json['username']
    _email = _json['email']
    _password = _json['password']
    
    # validate received values
    if _username and _email and _password and request.method == 'POST':
        # do not save password as a plain text
        _hashed_password = generate_password_hash(_password)
        # save details
        id = mongo.db.user.insert_one({'username': _username, 'email': _email, 'password': _hashed_password}).inserted_id
        response = jsonify('User added successfully.')
        response.status_code = 200
        return response
    else:
        return not_found()
    

@app.route('/api/auth/login', methods=['POST'])
def login():
    print("called register")
    _json = request.json
    _username = _json['username']
    _password = _json['password']

    # validate received values
    if _username and _password and request.method == 'POST':
        # check if user exists
        user = mongo.db.user.find_one({'username': _username})
        if user:
            # check if password matches
            if check_password_hash(user['password'], _password):
                user['_id'] = str(user['_id'])  # convert ObjectId to string
                response = jsonify(json_util.dumps(user))  # use json_util.dumps
                response.status_code = 200
                return response
            else:
                response = jsonify('Wrong password.')
                response.status_code = 401
                return response
        else:
            response = jsonify('User not found.')
            response.status_code = 404
            return response
    else:
        return not_found()
    
def get_first_four_sentences(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    return ' '.join(sentences[:2])


@app.route('/api/user/news', methods=['GET'])
def news():
    df=pd.read_csv(news_df)
    df = df.where(pd.notnull(df), None) 
    return jsonify(df.to_dict(orient='records'))


@app.route('/api/database', methods=['POST'])
def database():
    data = request.get_json()
    date_string = data['date'].replace("Z", "")
    request_date = pd.to_datetime(date_string)
    formatted_date = request_date.strftime('%Y-%m-%d')
    print(formatted_date)
    database_url = gold_df.loc[gold_df['date'] == formatted_date, 'database_url'].values[0]
    file_path = os.path.join(*database_url.split('/'))
    df_dataset=pd.read_csv(file_path)
    return jsonify(df_dataset.to_dict(orient='records'))

@app.route('/api/comparison', methods=['POST'])
def comparison():
    data = request.get_json()
    date_string = data['date'].replace("Z", "")
    request_date = pd.to_datetime(date_string)
    formatted_date = request_date.strftime('%Y-%m-%d')
    print(formatted_date)

    folder_path = 'BulkPredictionDatasets'
    result_df = pd.DataFrame(columns=['date', 'yhat_manipulation_smooth'])

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            filtered_df = df[df['ds'] == formatted_date]
            if not filtered_df.empty:
                filtered_df['date'] = filename.replace('.csv', '')
                result_df = pd.concat([result_df, filtered_df[['date', 'yhat_manipulation_smooth','yhat_lower_manipulation_smooth','yhat_upper_manipulation_smooth']]], ignore_index=True)
                result_df['date'] = pd.to_datetime(result_df['date'])
                result_df = result_df.sort_values(by='date')
                result_df = result_df.astype(str)
    print(result_df.head())
    return result_df.to_json(orient='records')

@app.route('/api/gold_price_history', methods=['GET'])
def gold_price_history():
    gold_ticker = 'GC=F'

    two_days_ago = datetime.datetime.now() - datetime.timedelta(days=1)
  
    end_date = two_days_ago.strftime('%Y-%m-%d')
    
    gold_data = yf.download(gold_ticker, start="2014-01-01", end=end_date)
    
    gold_data_reset = gold_data.reset_index()
   
    gold_data_selected = gold_data_reset[['Date', 'Close']]
    
    gold_data_list = gold_data_selected.values.tolist()
    
    gold_data_list = [[date.strftime('%m/%d/%Y'), close] for date, close in gold_data_list]

    return gold_data_list


@app.route('/api/real-data', methods=['POST'])
def real_data():
    print("togle start")
    train = train_df.replace({np.nan: 0})
    train['date'] = pd.to_datetime(train['date'] ,dayfirst=True, errors='coerce')
    train['gld_price_lkr'] = train['gld_price_lkr'].apply(ounce_lkr)

    return jsonify(train.to_dict(orient='records'))

def ounce_lkr(x):
    price = (x / 31.1035) * 8
    rounded_price = round(price / 100.0) * 100
    return rounded_price


@app.route('/api/forecast_prophet', methods=['POST'])
def gold_price_Predict():
    data = request.get_json()
    date_string = data['date'].replace("Z", "")
    request_date = pd.to_datetime(date_string)

    today_date = pd.to_datetime('today').normalize()
    dataset_last_given_date = pd.to_datetime('2024-06-12')

    day_count_difference_lastday_and_today = (today_date - dataset_last_given_date).days
    day_count_difference_requested_date_and_today = (request_date - today_date).days

    period=day_count_difference_lastday_and_today+day_count_difference_requested_date_and_today

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

    forecast=forecast[['ds','yhat','yhat_upper']]

    cols = [col for col in forecast.columns if col != 'ds']

    forecast[cols] = forecast[cols].applymap(ounce_lkr)

    forecast['yhat_manipulation'] = forecast['yhat_upper']+22000
    forecast['yhat_lower_manipulation']=forecast['yhat_upper']+13000
    forecast['yhat_upper_manipulation']=forecast['yhat_upper']+25000

    forecast['yhat_manipulation_smooth'] = forecast['yhat_manipulation'].rolling(window=7, min_periods=1).mean().round(-2)
    forecast['yhat_lower_manipulation_smooth'] = forecast['yhat_lower_manipulation'].rolling(window=5, min_periods=1).mean().round(-2)
    forecast['yhat_upper_manipulation_smooth'] = forecast['yhat_upper_manipulation'].rolling(window=5, min_periods=1).mean().round(-2)

    forecast['ds'] = pd.to_datetime(forecast['ds'], format='%a, %d %b %Y %H:%M:%S %Z')

    response_dataframe=forecast[["ds","yhat_manipulation_smooth","yhat_lower_manipulation_smooth","yhat_upper_manipulation_smooth"]]

    return jsonify(response_dataframe.to_dict(orient='records'))

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',debug=True, port=port)