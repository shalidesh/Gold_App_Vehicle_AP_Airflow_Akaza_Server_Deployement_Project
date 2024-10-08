import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from tqdm import tqdm 

links=[]
page=1

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }

link='https://www.kitco.com/'

response = requests.get(link,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

header = soup.find("div", class_='flex justify-between gap-2')

print(header)

# Find all h3 tags within the header
h3_tags = header.find_all("div",class_='text-right font-medium')
print(h3_tags)
# span_tags = header.find_all("span")
# print(span_tags)

texts = [h3.text for h3 in h3_tags[0]]
# spantexts = [h3.text for h3 in span_tags]
# bid, ask= texts
# change, performance = spantexts

print(texts)



