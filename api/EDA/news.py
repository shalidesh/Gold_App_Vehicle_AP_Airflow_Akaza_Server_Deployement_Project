import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from tqdm import tqdm 

links=[]
page=1

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

    # Convert the list of links into a DataFrame
df = pd.DataFrame(links, columns=['Links'])
df.to_csv("GOLDlinks.csv")


