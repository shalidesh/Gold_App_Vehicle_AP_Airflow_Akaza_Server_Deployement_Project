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
def model_creation_unique(source_table,data_table):
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
            df=df[["brand","model","year_of_manufacture","transmission","fuel_type","engine_capacity","vehicle_price"]]

            # Group by 'brand' and get unique 'model' values for each brand
            unique_models_df = df.groupby('brand')['model'].unique().reset_index()
            
            # Explode the unique models to have one model per row
            unique_models_df = unique_models_df.explode('model').reset_index(drop=True)

            unique_models_df = unique_models_df.applymap(lambda x: x.upper() if isinstance(x, str) else x)

            check_table(data_table)
            create_table(data_table, [
                        "Brand VARCHAR(255)",
                        "Model VARCHAR(255)"
                    ])
            populate_table(data_table, unique_models_df)
            upload_table_vehicle(data_table)
