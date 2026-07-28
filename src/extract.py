# Calls open-meteo's API to pull weather data using the request package
import requests
from typing import TypedDict

URL = "https://api.open-meteo.com/v1/forecast"

class WeatherParams(TypedDict):
    latitude: float
    longitude: float
    hourly: list[str]
    timezone: str
    forecast_days: int

params: WeatherParams = {
    "latitude": 48.13715,
    "longitude": 11.57612,
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "uv_index",
    ],
    "timezone": "Europe/Berlin",
    "forecast_days": 1,
}

def extract_weather_data(params: WeatherParams = params) -> dict:
    # Open-Meteo expects the hourly values as a comma-separated string
    # params["hourly"] = ",".join(params["hourly"])

    response = requests.get(URL, params=params, timeout=30)

    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()