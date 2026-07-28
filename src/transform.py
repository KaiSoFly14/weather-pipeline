# Takes in python json() object and transforms it into a pandas dataframe
import pandas as pd
from extract import extract_weather_data


data = extract_weather_data()

def transform_weather_data(data : dict = data) -> pd.DataFrame:
    df = pd.DataFrame(data["hourly"])
    print(df.head())
    return df

transformed_data = transform_weather_data()