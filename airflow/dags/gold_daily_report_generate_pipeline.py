from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from components.utils.send_email import success_email,failure_email
from components.gold.post_training.report_generate import generate_reports_daily



default_args = {
    'owner': 'sdeshan',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 10),
    'schedule_interval' : 'None',
    'email_on_failure': True,
    'email_on_success': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    dag_id="Daily_Gold_Report_Generate",
    default_args=default_args,
    schedule_interval="@daily"
)

daily_report_generate = PythonOperator(
    task_id='daily_report_generate',
    python_callable=generate_reports_daily,
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

#Set the order of tasks
daily_report_generate


