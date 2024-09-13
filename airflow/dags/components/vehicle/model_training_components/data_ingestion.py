import psycopg2
import pandas as pd
from components.utils.configs import host, database, port, user, password
from components.utils.database_table_creation import create_table,check_table,upload_table_vehicle,populate_table
import os
from sklearn.model_selection import train_test_split


def data_feeding(source_table):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:

            query = f"SELECT * FROM {source_table}"
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=column_names)

            make_list=df['brand'].unique().tolist()

            for make in make_list:
                train_data_tabel=f'{make}_train_data'

                df_data=df.groupby('brand').get_group(make)

                check_table(train_data_tabel)
                create_table(train_data_tabel, [
                            "Brand VARCHAR(255)",
                            "Posted_Date VARCHAR(255)",
                            "Model VARCHAR(255)",
                            "Year_of_Manufacture VARCHAR(255)",
                            "Transmission VARCHAR(255)",
                            "Fuel_Type VARCHAR(255)",
                            "Engine_Capacity VARCHAR(255)",
                            "Vehicle_Price VARCHAR(255)"
                        ])
                populate_table(train_data_tabel, df_data)
                upload_table_vehicle(train_data_tabel)

      

    