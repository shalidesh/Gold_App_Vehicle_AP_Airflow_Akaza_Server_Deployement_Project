from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from components.utils.send_email import success_email,failure_email
from components.vehicle.model_training_components.data_ingestion import data_feeding
from components.vehicle.model_training_components.data_transformation import transform_data
from components.vehicle.model_training_components.model_training import train_model 


default_args = {
    'owner': 'sdeshan',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 14),
    'schedule_interval' : 'None',
    'email_on_failure': True,
    'email_on_success': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    dag_id="Vehicle_Model_Training_Pipeline",
    default_args=default_args,
    schedule_interval="@daily"
)

data_ingestion = PythonOperator(
    task_id='data_ingestion',
    python_callable=data_feeding,
    op_kwargs={'source_table': 'ikman_post_data_preprocced'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

transformation_data = PythonOperator(
    task_id='data_transformation',
    python_callable=transform_data,
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training_honda = PythonOperator(
    task_id='model_training_honda',
    python_callable=train_model,
    op_kwargs={'source_table1': 'HONDA_train_data','train_model_name':'HONDA'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training_toyota = PythonOperator(
    task_id='model_training_toyota',
    python_callable=train_model,
    op_kwargs={'source_table1': 'TOYOTA_train_data','train_model_name':'TOYOTA'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training_nissan = PythonOperator(
    task_id='model_training_nissan',
    python_callable=train_model,
    op_kwargs={'source_table1': 'NISSAN_train_data','train_model_name':'NISSAN'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training_suzuki = PythonOperator(
    task_id='model_training_suzuki',
    python_callable=train_model,
    op_kwargs={'source_table1': 'SUZUKI_train_data','train_model_name':'SUZUKI'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training_micro = PythonOperator(
    task_id='model_training_micro',
    python_callable=train_model,
    op_kwargs={'source_table1': 'MICRO_train_data','train_model_name':'MICRO'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

model_training_mistubishi = PythonOperator(
    task_id='model_training_mistubishi',
    python_callable=train_model,
    op_kwargs={'source_table1': 'MITSUBISHI_train_data','train_model_name':'MITSUBISHI'}, 
    on_success_callback = success_email,
    on_failure_callback = failure_email,
    provide_context = True,
    dag=dag,
)

#Set the order of tasks
transformation_data.set_upstream(data_ingestion)
model_training_honda.set_upstream(transformation_data)
model_training_toyota.set_upstream(model_training_honda)
model_training_nissan.set_upstream(model_training_toyota)
model_training_suzuki.set_upstream(model_training_nissan)
model_training_micro.set_upstream(model_training_suzuki)
model_training_mistubishi.set_upstream(model_training_micro)


