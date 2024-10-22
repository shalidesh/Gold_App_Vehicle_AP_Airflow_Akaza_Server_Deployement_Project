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
from airflow.utils.email import send_email
from airflow.hooks.base_hook import BaseHook

email_artifacts=os.path.join("dags","components","gold","model_training","training_data","df_interpolated_2024_10_21.csv")


def mail_sending(source_table, **kwargs):
    # Email configuration
    sender_email = "sdeshan970bis@gmail.com"
    receiver_emails = ["shalika.ariyarathna@cdbnet.lk"]
    subject = "Weekly Report"
    body = "Please find the attached weekly report."

    # Path to the CSV file
    attachment_path = email_artifacts
    attachment_name = os.path.basename(attachment_path)

    # Check if the file exists
    if not os.path.exists(attachment_path):
        raise FileNotFoundError(f"The file {attachment_path} does not exist.")

    # Read the CSV file content
    with open(attachment_path, "rb") as attachment:
        attachment_content = attachment.read()

    email_content = {
        'subject': subject,
        'html_content': body,
        'files': [attachment_path]  # Pass the file path directly
    }

    try:
        send_email(to=receiver_emails, **email_content)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

    