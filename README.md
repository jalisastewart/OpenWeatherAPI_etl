This project is a simple Extract, Transform, Load (ETL) pipeline for retrieving current weather data from the OpenWeatherMap API for a specified city, processing it, and saving it to a CSV file.

Prerequisites
Before running the code, make sure you have the following installed:

Python 3.x
Pandas library (pip install pandas)
Requests library (pip install requests)

Usage
Obtain OpenWeatherMap API Key: Sign up for an API key on the OpenWeatherMap website if you haven't already. Save your API key in a file named credentials.txt in the same directory as the code. For example:

Copy code
YOUR_API_KEY
Set City Name: Modify the city_name variable in the code to specify the city for which you want to retrieve weather data. For example:

python
Copy code
city_name = "Houston"
Run the Code: Execute the script by running the following command in your terminal or command prompt:

Copy code
python weather_etl.py
Check Output: After running the script, a CSV file named current_weather_data_houston.csv will be created in the same directory, containing the retrieved weather data.

License
This project is licensed under the MIT License - see the LICENSE file for details.

