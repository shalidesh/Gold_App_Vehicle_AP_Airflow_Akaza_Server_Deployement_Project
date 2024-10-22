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

# Scrape the sun website
def scrape_links():

    headers = {
        "User-Agent": "web-scrapping",
        "From": "youremail@example.com"  # Include your email so the website owner can contact you if necessary
    }

    links=[]
    pages=[]
    transmission_list=[]
    fuel_type_list=[]

    page=1

    make=['toyota','honda','nissan','suzuki','micro','mitsubishi']

    # make=['micro']
    transmission=['automatic','manual','tiptronic']
    fuel_type=['petrol','diesel','hybrid','electric']

    for m in make:
        for t in transmission:
            for f in fuel_type:
                isHaveNextPage=True
                while(isHaveNextPage):
                    target_url=f'https://ikman.lk/en/ads/sri-lanka/cars/{m}?sort=date&order=desc&buy_now=0&urgent=0&page={page}&tree.brand={m}&enum.transmission={t}&enum.fuel_type={f}'
                    url=requests.get(target_url,headers=headers)
                    soup=BeautifulSoup(url.text,'lxml')
                    product=soup.find('ul',class_="list--3NxGO")

                    # If no results found, stop the loop
                    if product is None or len(product.find_all("li", class_="normal--2QYVk gtm-normal-ad")) == 0 :
                        isHaveNextPage = False
                        page=1
                        print("page is no content-----------------")
                        break

                    for item in tqdm(product.find_all("li", class_="normal--2QYVk gtm-normal-ad")):
                        anchor = item.find('a')
                        if anchor is not None:
                            link = anchor.get('href')
                            link=f"https://ikman.lk{link}"
                            print("-------------------------------------------")
                            print(link)
                            print("-------------------------------------------")
                            links.append((link))
                            pages.append(str(page))
                            transmission_list.append(str(t))
                            fuel_type_list.append(str(f))

                        else:
                            print('No anchor tag found in the item.')

                    page+=1

                    time.sleep(0.5) 

    links_df = pd.DataFrame({'Link': links})

    check_table("ikman_vehicle_post_links")
    create_table("ikman_vehicle_post_links", ["Link VARCHAR(255)"])
    populate_table("ikman_vehicle_post_links", links_df)
    # upload_table_vehicle('ikman_vehicle_post_links')