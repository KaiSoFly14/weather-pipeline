# Calls open-meteo's API to pull weather data using the request package
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
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

print(params["hourly"])

# Open-Meteo expects the hourly values as a comma-separated string
params["hourly"] = ",".join(params["hourly"])

print(params["hourly"])

response = requests.get(url, params=params)

data = response.json()

print(data)