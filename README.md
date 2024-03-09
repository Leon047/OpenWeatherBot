# OpenWeatherBot

> Demo telegram bot


## Description 

WeatherInfoBot is a convenient and fast Telegram bot that provides current weather information for a selected country. 
Thanks to integration with the Open Weather API, the bot can provide real-time climate data based on the country name you enter.

Key Features:
* Get Weather by Country: Enter the country name, and the bot will provide you with the current weather with detailed information such as temperature, humidity, wind speed, and other essential parameters.

* Visual Representation: Receive a visual representation of the current weather with icons and charts to better understand the climatic conditions.

* Interactive Interaction: The bot allows interaction with weather data and provides additional options for more detailed inquiries.


## Used 
<div align='center'>

[![Python](https://img.shields.io/static/v1?label=Python&message=v3.11.x&color=green)](https://www.python.org/downloads/release/python-394/)
[![Aiogram](https://img.shields.io/static/v1?label=Aiogram&message=v3.4.1&color=blue)](https://docs.aiogram.dev/en/latest/)

</div>

API:
- [Open Weather API](https://openweathermap.org/api)


## Installation

Clone the repository:
```bash
git clone https://github.com/Leon047/OpenWeatherBot.git
```


To add to the .env file.:

BOT_TOKEN
```bash
https://t.me/BotFather
```

OPEN_WEATHER_KEY
```bash
https://openweathermap.org/
```

Set environment variables:
```bash
source .env
```


## Using venv 

Install dependencies:
```bash
pip install --upgrade -r requirements.txt
```

Run the bot:
```bash
python run.py
```


## Using Docker

Docker build:
```bash
docker build --no-cache --build-arg BOT_TOKEN=$BOT_TOKEN --build-arg OPEN_WEATHER_KEY=$OPEN_WEATHER_KEY -t owbot .
```
Docker run:
```bash
docker run -i -t -p 80:80 owbot
```
