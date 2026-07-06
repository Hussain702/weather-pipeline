import pandas as pd


def transform():

    df = pd.read_csv("/opt/airflow/data/weather_raw.csv")

    # remove duplicate cities
    df.drop_duplicates(subset="city", inplace=True)

    # convert description to uppercase
    df["description"] = df["description"].str.upper()

    # create a new column
    df["temperature_fahrenheit"] = df["temperature"] * 9/5 + 32

    # classify weather

    df["temperature_status"] = df["temperature"].apply(

        lambda x: "Cold" if x < 10
        else "Warm" if x < 20
        else "Hot"

    )

    # round temperature

    df["temperature"] = df["temperature"].round(1)

    df.to_csv("/opt/airflow/data/weather_transformed.csv", index=False)

    print("Transformation completed.")