# Task 3
# The Weather app
# Write a console application which takes as an input a city name and
# returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use

import requests
from configparser import ConfigParser

location = input('Please enter the city: ')
URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
API_KEY = config['key']['api']
response = requests.get(URL.format(location,API_KEY))

if not response.ok:
    raise ConnectionError('City is not found!')

data = response.json()

city = data['name']
country = data['sys']['country']
temperature = data['main']['temp']
humidity = data['main']['humidity']
weather = data['weather'][0]['description']

print(f'''
City: {city}
Country: {country}
Temperature: {round(temperature - 273.15)}°C
Humidity: {humidity}%
Weather description: {weather}
HAVE A NICE DAY!
''')






