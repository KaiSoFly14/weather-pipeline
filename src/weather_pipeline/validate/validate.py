# check for missing or invalid data

# What should I be looking for to validate a data set?
# - Missing columns
# - Missing values
# - Do my data types make sense?
# - Invalid ranges (e.g., negative UV index or humidity > 100%)
# - Check shape of tensor...? could check number of columbns but not sure if I want to hard code these values 

# Make this into a function so that I can create a package in a cleaner way

def validate_temperature(temperature: float | None) -> None:
    if temperature is None:
        raise ValueError("Missing temperature value")

def validate_coordinates(latitude: float, longitude: float) -> None:
    if not -90 <= latitude <= 90:
        raise ValueError("Latitude out of range")

    if not -180 <= longitude <= 180:
        raise ValueError("Longitude out of range")

def validate_humidity(humidity: float | None) -> None:
    if not 0 <= humidity <= 100:
        raise ValueError("Humidity is out of range")
