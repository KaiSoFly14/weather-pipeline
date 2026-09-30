from weather_pipeline.extract import extract_weather_data
from weather_pipeline.transform import transform_weather_data
from weather_pipeline.validate import validate_weather_data


def run_pipeline():
    raw_data = extract_weather_data()

    transformed_data = transform_weather_data(raw_data)

    validate_weather_data(transformed_data)

    return transformed_data


if __name__ == "__main__":
    run_pipeline()