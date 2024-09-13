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
from components.utils.database_table_creation import create_table,check_table,populate_table,upload_table_gold
# import nltk
# nltk.download('punkt')

# def get_first_four_sentences(text):
#     sentences = nltk.tokenize.sent_tokenize(text)
#     return ' '.join(sentences[:2])

def scrape_gold_news_content_from_urls(source_table,data_table):

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
            for link in df['link']:
                try:

                    print("##########################################")

                    post_links.append(link)
                    print(f'link --- {link}')
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

                    print(f'title --- {title}')

                    #get Posted Date
                    date = soup.find("time").get_text()
                    post_date.append(date)


                    print(f'date --- {date}')

                    # Find the article image
                    content = soup.find("article")
                    image = content.find("img")
                    link = image.get("src")
                    post_image.append(link)

                    print(f'post_image --- {link}')

                    # Find the article paragraph
                    articleBody = soup.find(id='articleBody')
                    p_tags = articleBody.find_all('p') if articleBody else []

                    text_found = False

                    for p in p_tags:
                        # print(f'length of p tags-$$$$$$$$$$$$$${len(p_tags)}')
                        text = p.text.strip() 
                        if text:
                            print(f'sample_text --- {text}')
                            sample_text.append(text)
                            text_found = True
                            break

                    if not text_found:
                        print(f'sample_text --- ')
                        sample_text.append(" ")

                       
                except Exception as e:
                    print("something wrong",e)

            print(f'lenfth of date ---{len(post_date)}')
            print(f'length of links ---{len(post_links)}')
            print(f'length of posted_title ---{len(posted_title)}')
            print(f'length of images ---{len(post_image)}')
            print(f'length of text --{len(sample_text)}')


            # Create a DataFrame
            df = pd.DataFrame({
                "posted_date":post_date,
                "post_link":post_links,
                "posted_title": posted_title,
                "post_img": post_image,
                "sample_text":sample_text
                
            })

            # df['sample_text'] = df['sample_text'].apply(get_first_four_sentences)


            check_table(data_table)
            create_table(data_table, 
                         ["posted_date VARCHAR(255)",
                          "post_link VARCHAR(255)",
                          "posted_title VARCHAR(255)",
                          "post_img VARCHAR(255)",
                          "sample_text TEXT"
                        ]),            
            populate_table(data_table, df)
            upload_table_gold(data_table)
        
    
    
