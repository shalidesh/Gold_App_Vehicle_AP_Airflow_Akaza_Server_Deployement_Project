import psycopg2
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
import time
from components.utils.database_table_creation import create_table,check_table,populate_table,upload_table_gold


# Scrape the sun website
def scrape_gold_news_urls():
    links=[]
    isHaveNextPage=True

    while(isHaveNextPage):

        target_url=f'https://www.kitco.com/'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        url = requests.get(target_url, headers=headers)
        
        soup=BeautifulSoup(url.text,'html.parser')
        content = soup.find("div", class_='mb-3')
        postlinks = content.find_all("div", class_='ListItemOneLine_container__x_mFN')

        for i, row in enumerate(postlinks):
            anchor = row.find('a')
            if anchor is not None:
                link = anchor.get('href')
                link=f"https://www.kitco.com{link}"
                links.append(link)
                
            else:
                print('No anchor tag found in the item.')

        isHaveNextPage=False
        time.sleep(1) 

    links_df = pd.DataFrame(links, columns=['link'])

    check_table("gold_news_urls")
    create_table("gold_news_urls", ["link VARCHAR(255)"])
    populate_table("gold_news_urls", links_df)
    upload_table_gold("gold_news_urls")
