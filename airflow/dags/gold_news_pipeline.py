from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from components.gold.news_scraping.post_links_extraction import scrape_gold_news_urls
from components.utils.send_email import success_email,failure_email
from components.gold.news_scraping.post_data_extraction import scrape_gold_news_content_from_urls

default_args = {
    'owner': 'sdeshan',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 28),
    'schedule_interval' : 'None',
    'email_on_failure': True,
    'email_on_success': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    dag_id="Gold_News_pipeline",
    default_args=default_args,
    schedule_interval='0 0 * * *'
)



gold_news_urls = PythonOperator(
    task_id='scrape_gold_news',
    python_callable=scrape_gold_news_urls,
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

gold_news_content_from_urls = PythonOperator(
    task_id='scrape_gold_news_content_from_urls',
    python_callable=scrape_gold_news_content_from_urls,
    op_kwargs={'source_table': 'gold_news_urls','data_table': 'gold_post_data'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)


# Set the order of tasks
gold_news_content_from_urls.set_upstream(gold_news_urls)


