import pandas as pd
import psycopg2
import os
from datetime import date


def load():

    df = pd.read_csv("/opt/airflow/data/weather_transformed.csv")

    conn = psycopg2.connect(

        host="postgres",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")

    )

    cur = conn.cursor()

    query = """
    INSERT INTO weather
    (city, temperature, humidity, weather_description, date)
    VALUES (%s,%s,%s,%s,%s)
    """

    for _, row in df.iterrows():

        cur.execute(query, (

            row["city"],
            row["temperature"],
            row["humidity"],
            row["description"],
            date.today()

        ))

    conn.commit()

    cur.close()
    conn.close()

    print("Data loaded into PostgreSQL.")