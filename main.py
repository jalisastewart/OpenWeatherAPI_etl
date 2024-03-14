# Import necessary libraries
import json
from datetime import datetime
import pandas as pd 
import requests

# Set city name for which weather data is to be retrieved
city_name = "Houston"

# Define the base URL for the OpenWeatherMap API
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

# Read API key from a separate file
with open("credentials.txt", 'r') as f:
    api_key = f.read()

# Construct the full URL with the city and API key
full_url = base_url + city_name + "&APPID=" + api_key

# Function to convert temperature from Kelvin to Fahrenheit
def kelvin_to_fahrenheit(temp_in_kelvin):
    temp_in_fahrenheit = (temp_in_kelvin - 273.15) * (9/5) + 32
    return temp_in_fahrenheit

# Retrieve weather data from the API
def etl_weather_data(url):
    r = requests.get(full_url)
    data = r.json( )

    # Extract relevant weather data from the API response
    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_fahrenheit = kelvin_to_fahrenheit(data["main"]["temp"])
    feels_like_fahrenheit = kelvin_to_fahrenheit(data["main"]["feels_like"])
    min_temp_fahrenheit = kelvin_to_fahrenheit(data["main"]["temp_min"])
    max_temp_fahrenheit = kelvin_to_fahrenheit(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Convert UNIX timestamps to datetime objects
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

    # Organize the extracted data into a dictionary
    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (F)": temp_fahrenheit,
                        "Feels Like (F)": feels_like_fahrenheit,
                        "Minimum Temp (F)": min_temp_fahrenheit,
                        "Maximum Temp (F)": max_temp_fahrenheit,
                        "Pressure": pressure,
                        "Humidity": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)": sunrise_time,
                        "Sunset (Local Time)": sunset_time
                        }

    # Convert the dictionary into a list (required for DataFrame creation)
    transformed_data_list = [transformed_data]

    # Create a DataFrame from the list of transformed data
    df_data = pd.DataFrame(transformed_data_list)
    # print(df_data)

    # Save the DataFrame to a CSV file
    df_data.to_csv("current_weather_data_houston.csv", index = False)

if __name__ == '__main__':
    etl_weather_data(url = full_url)