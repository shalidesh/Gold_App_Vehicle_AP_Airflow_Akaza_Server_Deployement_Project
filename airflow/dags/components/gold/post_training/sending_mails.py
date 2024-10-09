import psycopg2
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
from components.utils.database_table_creation import create_table,check_table
from components.utils.configs import host, database, port, user, password
from datetime import datetime
from airflow.operators.email import EmailOperator
import os

email_artifacts=os.path.join("dags","components","gold","model_training","training_data","df_interpolated.csv")

def send_email():
    task_status = 'Success'
    subject = f'Gold Forecasting Result'
    body = "Gold Forecasting Result"
    
    to_emails = ['deshanariyarathna@gmail.com','shalika.ariyarathna@gmail.com']

    email_operator = EmailOperator(
        task_id='send_email',
        to=to_emails,
        subject=subject,
        html_content=body,
        files=[email_artifacts]
    )
    email_operator.execute()


def mail_sending(source_table):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            query = f"SELECT * FROM {source_table}"
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            df = pd.DataFrame(rows, columns=column_names)
            print(df.head())
            send_email()
    
    