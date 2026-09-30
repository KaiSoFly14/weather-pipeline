# Takes in python json() object and transforms it into a pandas dataframe
import pandas as pd

def transform_weather_data(data : dict) -> pd.DataFrame:
    df = pd.DataFrame(data["hourly"])
    print(df.head())
    return df
