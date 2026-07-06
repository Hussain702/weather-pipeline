from airflow.decorators import dag, task
from datetime import datetime

from etl.extract import extract
from etl.transform import transform
from etl.load import load


default_args = {
    "start_date": datetime(2024, 1, 1)
}


@dag(
    dag_id="weather_etl",
    default_args=default_args,
    schedule="@daily",
    catchup=False
)
def weather_dag():

    @task
    def extraction():
        extract()

    @task
    def transformation():
        transform()

    @task
    def loading():
        load()

    extract_task = extraction()
    transform_task = transformation()
    load_task = loading()

    extract_task >> transform_task >> load_task


weather_dag()