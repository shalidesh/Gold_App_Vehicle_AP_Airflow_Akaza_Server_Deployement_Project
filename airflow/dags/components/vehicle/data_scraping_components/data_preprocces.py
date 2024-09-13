import psycopg2
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
import time
import re
from pandas import DataFrame
from components.utils.database_table_creation import create_table,check_table,upload_table_vehicle,populate_table
from components.utils.configs import host, database, port, user, password

# Scrape the sun website
def data_preprocces(source_table,data_table):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            # Prepare the SQL query
            query = f"SELECT * FROM {source_table}"
            # Execute the query
            cur.execute(query) 
            # Fetch all the rows
            rows = cur.fetchall()
            # Get the column names from the cursor description
            column_names = [desc[0] for desc in cur.description]
            # Create a DataFrame from the rows and column names
            df = pd.DataFrame(rows, columns=column_names)
            df=df[["brand","posted_date","model","year_of_manufacture","transmission","fuel_type","engine_capacity","vehicle_price"]]

            columns_to_check = ["brand","posted_date","model","year_of_manufacture","transmission","fuel_type","engine_capacity","vehicle_price"]

            # Filter rows where any of the specified columns have "0" values
            df = df[~df[columns_to_check].isin(['0']).any(axis=1)]

            df['posted_date'] = df['posted_date'].str.extract(r'(\d{2} \w{3})')

            # Preprocess the 'Engine Capacity' column
            df['engine_capacity'] = df['engine_capacity'].str.replace(',', '').str.replace(' cc', '')

            # Preprocess the 'mileage' column
            df['vehicle_price'] = df['vehicle_price'].replace('Negotiable','Rs 0')
            df['vehicle_price'] = df['vehicle_price'].str.replace(',', '').str.replace('Rs ', '')

            df.astype(str)
            print(df.head(5))
            df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
            print(df.head(5))
    
    
    # check_table(data_table)
    create_table(data_table, [
                "Brand VARCHAR(255)",
                "Posted_Date VARCHAR(255)",
                "Model VARCHAR(255)",
                "Year_of_Manufacture VARCHAR(255)",
                "Transmission VARCHAR(255)",
                "Fuel_Type VARCHAR(255)",
                "Engine_Capacity VARCHAR(255)",
                "Vehicle_Price VARCHAR(255)"
            ])
    populate_table(data_table, df)
    upload_table_vehicle(data_table)
