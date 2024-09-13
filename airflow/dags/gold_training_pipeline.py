from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from components.utils.send_email import success_email,failure_email

from components.gold.model_training.data_scraping import scrape_data
from components.gold.model_training.data_preprocessing import preprocess_data
from components.gold.model_training.model_training import forecast_model_training


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
    dag_id="Gold_training_Pipeline",
    default_args=default_args,
    schedule_interval='0 0 * * *'
)



data_scraping= PythonOperator(
    task_id='scrape_time_series_data',
    python_callable=scrape_data,
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

data_preprocess= PythonOperator(
    task_id='preprocess_the_extracted_data',
    python_callable=preprocess_data,
    op_kwargs={'source_table': 'scrape_data_table','data_table': 'preprocesed_data_tables'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training = PythonOperator(
    task_id='model_training',
    python_callable=forecast_model_training,
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)


# Set the order of tasks
data_preprocess.set_upstream(data_scraping)
model_training.set_upstream(data_preprocess)
