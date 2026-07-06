from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract
from etl.transform import transform
from etl.load import load


default_args = {

    "start_date": datetime(2024,1,1)

}

with DAG(

    dag_id="weather_etl",

    default_args=default_args,

    schedule_interval="@daily",

    catchup=False

) as dag:

    extract_task = PythonOperator(

        task_id="extract",

        python_callable=extract

    )

    transform_task = PythonOperator(

        task_id="transform",

        python_callable=transform

    )

    load_task = PythonOperator(

        task_id="load",

        python_callable=load

    )

    extract_task >> transform_task >> load_task