# OpenWeatherBot
## Demo Telegram Bot

## Used by
* Python 3.9.4
* Aiogram
* Docker

## Install Docker 
* https://docs.docker.com/install/linux/docker-ce/ubuntu/

## For project deployment:
* docker build -t owbot .
* docker build --no-cache --build-arg BOT_TOKEN --build-arg OPEN_WEATHER_KEY -t owbot .
* docker run -i -t -p 80:80 owbot    
