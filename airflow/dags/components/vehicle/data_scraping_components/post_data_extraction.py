import psycopg2
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
import time
import re
from components.utils.configs import host, database, port, user, password
from pandas import DataFrame
from components.utils.database_table_creation import create_table,check_table,upload_table_vehicle,populate_table


def scarpe_and_save(source_table,data_table):

    new_column_names = {
        "Post_Link": "Post_Link",
        "Posted Title": "Posted_Title",
        "Posted Date": "Posted_Date",
        "Brand": "Brand",
        "Model": "Model",
        "Grade": "Grade",
        "Trim / Edition":"Trim_Edition",
        "Year of Manufacture": "Year_of_Manufacture",
        "Condition": "Condition",
        "Transmission": "Transmission",
        "Body type": "Body_type",
        "Fuel type": "Fuel_type",
        "Engine capacity": "Engine_capacity",
        "Mileage": "Mileage",
        "Vehicle Price": "Vehicle_Price"
    }

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

           # Initialize an empty list to store car data
            car_data_list = []

            # Iterate over the links
            for link in tqdm(df['link']):

                car_info = {
                "Post_Link": "0",
                "Posted Title": "0",
                "Posted Date": "0",
                "Brand": "0",
                "Model": "0",
                "Grade": "0",
                "Trim / Edition":"0",
                "Year of Manufacture": "0",
                "Condition": "0",
                "Transmission": "0",
                "Body type": "0",
                "Fuel type": "0",
                "Engine capacity": "0",
                "Mileage": "0",
                "Vehicle Price": "0"
                }
                try:

                    headers = {
                        "User-Agent": "web-scrapping",
                        "From": "youremail@example.com"  # Include your email so the website owner can contact you if necessary
                    }

                    car_info['Post_Link']=link
                    # Send a GET request
                    response = requests.get(link,headers=headers)

                    # Create a BeautifulSoup object and specify the parser
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Find the header
                    header = soup.find("div", class_='title-wrapper--1lwSc')

                    # Extract the title
                    posted_title_name = header.find('h1').get_text() if header and header.find('h1') else ""
                    car_info['Posted Title']=posted_title_name

                    # Extract the posted date
                    posted_date = header.find("div", class_='subtitle-wrapper--1M5Mv') if header else None
                    posted_date_str = re.sub('<[^<]+?>', '', str(posted_date)) if posted_date else ""
                    car_info['Posted Date']=posted_date_str

                    vehicle_price = soup.find("div", class_='amount--3NTpl')
                    price=vehicle_price.get_text() if vehicle_price else ""

                    # price_list.append(price)
                    car_info['Vehicle Price']=price

                    # Find the vehicle details
                    vehicle_details = soup.find("div", class_='ad-meta--17Bqm justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-wrap--2PCx8 flex-direction-row--27fh1 flex--3fKk1')
                    # vehicle_details_table_rows = vehicle_details.find_all("div", class_='two-columns--19Hyo full-width--XovDn justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-nowrap--3IpfJ flex-direction-row--27fh1 flex--3fKk1') if vehicle_details else []
                    vehicle_details_table_rows = vehicle_details.find_all("div", class_='full-width--XovDn justify-content-flex-start--1Xozy align-items-normal--vaTgD flex-wrap-nowrap--3IpfJ flex-direction-row--27fh1 flex--3fKk1') if vehicle_details else []


                    for row in vehicle_details_table_rows:
                        tag = row.find('div', class_='word-break--2nyVq label--3oVZK')
                        label=tag.get_text()
                        tag1 = row.find('div', class_='word-break--2nyVq value--1lKHt')
                        value=tag1.get_text()
                        
                        car_info[label.strip("' :")]=value

                    car_data_list.append(car_info)

                except Exception as e:
                    print("something wrong")

                time.sleep(1) 

            # Close the cursor and connection
            conn.commit()

            # Create a DataFrame from the collected data
            car_df = pd.DataFrame(car_data_list)
            car_df.rename(columns=new_column_names, inplace=True)
            car_df=car_df.astype(str)

            check_table(data_table)
            create_table(data_table, [
                "Post_Link VARCHAR(255)",
                "Posted_Title VARCHAR(255)",
                "Posted_Date VARCHAR(255)",
                "Brand VARCHAR(255)",
                "Model VARCHAR(255)",
                "Grade VARCHAR(255)",
                "Trim_Edition VARCHAR(255)",
                "Year_of_Manufacture VARCHAR(255)",
                "Condition VARCHAR(255)",
                "Transmission VARCHAR(255)",
                "Body_Type VARCHAR(255)",
                "Fuel_Type VARCHAR(255)",
                "Engine_Capacity VARCHAR(255)",
                "Mileage VARCHAR(255)",
                "Vehicle_Price VARCHAR(255)"
            ])
                                    
            populate_table(data_table, car_df)
            upload_table_vehicle(data_table)
        
    
    
