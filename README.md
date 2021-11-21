# OpenWeatherBot
## Demo Telegram Bot

## Using api
* https://openweathermap.org/api

## Used by
* Python 3.9.4
* Aiogram 2.12.1
* Docker

## Install Docker 
* https://docs.docker.com/install/linux/docker-ce/ubuntu/

## For project deployment:
* source setenv.sh
* sudo docker build --no-cache --build-arg BOT_TOKEN=$BOT_TOKEN --build-arg OPEN_WEATHER_KEY=$OPEN_WEATHER_KEY -t owbot .
* sudo docker run -i -t -p 80:80 owbot

# bot name
* @BotUserOpenWeatherBotBot

  <p align="center"> 
    <img src="https://user-images.githubusercontent.com/43421023/133983926-af29c5a3-32f7-42c2-b0a0-5fb91ffa8a6b.png" alt="OpenWeatherBot">
  </p>
