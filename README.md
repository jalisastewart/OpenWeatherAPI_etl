This project is a simple Extract, Transform, Load (ETL) pipeline for retrieving current weather data from the OpenWeatherMap API for a specified city, processing it, and saving it to a CSV file. It was developed using a remote Visual Studio Code (VS Code) instance on an Amazon EC2 (Elastic Compute Cloud) server.

Prerequisites
Before running the code, make sure you have the following installed:

Python 3.x
Pandas library (pip install pandas)
Requests library (pip install requests)
Usage
Set Up Remote VS Code Instance on EC2:

Launch an EC2 instance with Ubuntu or any Linux distribution.
Install and configure SSH access to the EC2 instance.
Install VS Code Server on the EC2 instance by following the instructions provided in the VS Code Remote Development documentation.
Connect to the EC2 instance using VS Code Remote SSH extension.
Clone the Repository:

Clone this repository to your remote VS Code instance:
bash
Copy code
git clone https://github.com/jalisastewart/openweather_etl.git

Obtain OpenWeatherMap API Key:
Sign up for an API key on the OpenWeatherMap website if you haven't already.

Save your API key in a file named credentials.txt in the same directory as the code. For example:
Copy code
YOUR_API_KEY

Set City Name:
Modify the city_name variable in the code to specify the city for which you want to retrieve weather data. For example:
python
Copy code
city_name = "Houston"
Run the Code:

Execute the script by running the following command in your remote VS Code terminal:
Copy code
python weather_etl.py

Check Output:
After running the script, a CSV file named current_weather_data_houston.csv will be created in the same directory, containing the retrieved weather data.

Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.
