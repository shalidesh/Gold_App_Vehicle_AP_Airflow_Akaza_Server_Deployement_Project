from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from components.utils.send_email import success_email,failure_email

from components.gold.model_training.data_scraping import scrape_data
from components.gold.model_training.data_preprocessing import preprocess_data
from components.gold.model_training.model_training import forecast_model_training
from components.gold.post_training.sending_mails import mail_sending
from components.gold.post_training.report_generate import generate_reports


default_args = {
    'owner': 'sdeshan',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 8),
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
    op_kwargs={'source_table': 'scrape_gold_data_table','data_table': 'preprocesed_gold_data_tables'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training = PythonOperator(
    task_id='model_training',
    python_callable=forecast_model_training,
    op_kwargs={'source_table': 'preprocesed_gold_data_tables'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

# weekly_report_generate = PythonOperator(
#     task_id='weekly_report_generate',
#     python_callable=generate_reports,
#     op_kwargs={'target_table': 'weekly_report'}, 
#     on_success_callback = success_email,
#     on_failure_callback = failure_email,
#     provide_context = True,
#     dag=dag,
# )

send_mails = PythonOperator(
    task_id='send_mails',
    python_callable=mail_sending,
    op_kwargs={'source_table': 'weekly_report'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)


# Set the order of tasks
data_preprocess.set_upstream(data_scraping)
model_training.set_upstream(data_preprocess)
# weekly_report_generate.set_upstream(model_training)
send_mails.set_upstream(model_training)
