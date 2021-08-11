import pendulum
from airflow import models
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 8, 9, tzinfo=KST),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with models.DAG(
    dag_id='test', description='write date and, hello airflow!',
    schedule_interval='*/10 * * * *', # 10분마다 한번 씩 반복
    default_args=default_args,
    catchup=False
) as dag:
    
    t1 = BashOperator(
        task_id='write_date',
        bash_command='echo "data now : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)" >> ~/airflow/test.txt',
        dag=dag
    )
    
    t2 = BashOperator(
        task_id='write_hello_airflow',
        bash_command='echo "hello airflow!" >> ~/airflow/test.txt',
        dag=dag
    )
    
    t1 >> t2