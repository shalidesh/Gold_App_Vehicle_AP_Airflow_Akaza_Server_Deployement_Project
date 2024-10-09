import psycopg2
from datetime import datetime, timedelta
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
from components.utils.database_table_creation import create_table,check_table,populate_table,upload_table_gold

dataset_path=os.path.join("dags","components","gold","model_training","training_data","df_interpolated.csv")

def preprocess_data(source_table,data_table):

    df=pd.read_csv(dataset_path)
    df=df.astype(str)

    check_table(data_table)
    create_table(data_table, 
                    ["Date VARCHAR(255)",
                    "gold_lkr VARCHAR(255)",
                    "gold_price_usd VARCHAR(255)",
                    "silver_price VARCHAR(255)",
                    "sp_500_index  VARCHAR(255)",
                    "nyse_com_index VARCHAR(255)",
                    "usd_selling_exrate VARCHAR(255)",
                    "gold_futures VARCHAR(255)",
                    "effr VARCHAR(255)"
                ]),            
    populate_table(data_table, df)
    upload_table_gold(data_table)

    
