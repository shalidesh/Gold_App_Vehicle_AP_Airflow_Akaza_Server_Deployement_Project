import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from tqdm import tqdm 

# Read the CSV file
df = pd.read_csv('GOLDlinks.csv')

# Initialize empty lists
post_links=[]
posted_title = []
post_image=[]
post_date=[]
sample_text=[]

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

# Iterate over the links
for link in df['Links']:
    try:

        print("--------")

        post_links.append(link)
        response = requests.get(link,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')


        #get post title
        header = soup.find("div", class_='md:w-[calc(100%_-_190px)] md:pl-10')
        if header is None:
            header2 = soup.find("div", class_='w-[calc(100%_-_190px)] pl-10')
            title=header2.find('h1').get_text() 
        else:
            title=header.find('h1').get_text() 
        posted_title.append(title)

        print(title)


        #get Posted Date
        date = soup.find("time").get_text()
        post_date.append(date)


        print(date)


        # Find the article image
        content = soup.find("article")
        image = content.find("img")
        link = image.get("src")
        post_image.append(link)

        print(link)

        # Find the article paragraph
        articleBody = soup.find(id='articleBody')
        p_tags = articleBody.find_all('p') if articleBody else []
        for p in p_tags:
            text = p.text.strip() 
            if text:
                print(text)
                sample_text.append(text)
                break
        else:
            text = None
                
            
    except Exception as e:
        print("something wrong",e)

# Create a DataFrame
df = pd.DataFrame({
    "posted_date":post_date,
    "post_link":post_links,
    "posted_title": posted_title,
    "post_img": post_image,
    "sample_text":sample_text
    
})

# Save the DataFrame to a CSV file
df.to_csv('news.csv', index=False)

