import requests
import pandas as pd
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

UK_CITIES = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904},
    {"name": "Manchester", "lat": 53.4808, "lon": -2.2426},
    {"name": "Glasgow", "lat": 55.8642, "lon": -4.2518},
    {"name": "Liverpool", "lat": 53.4084, "lon": -2.9916},
    {"name": "Leeds", "lat": 53.8008, "lon": -1.5491},
    {"name": "Sheffield", "lat": 53.3811, "lon": -1.4701},
    {"name": "Bristol", "lat": 51.4545, "lon": -2.5879},
    {"name": "Newcastle", "lat": 54.9784, "lon": -1.6174},
    {"name": "Nottingham", "lat": 52.9548, "lon": -1.1581}
]


def extract():

    weather_list = []

    for city in UK_CITIES:

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}&units=metric"

        response = requests.get(url).json()

        weather_list.append({

            "city": city["name"],
            "temperature": response["main"]["temp"],
            "humidity": response["main"]["humidity"],
            "description": response["weather"][0]["description"]

        })

    df = pd.DataFrame(weather_list)

    os.makedirs("/opt/airflow/data", exist_ok=True)

    df.to_csv("/opt/airflow/data/weather_raw.csv", index=False)

    print("Raw weather data saved.")