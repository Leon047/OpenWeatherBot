# OpenWeatherBot

> Demo telegram bot


## Description 

***The Telegram bot allows you to receive meteorological location data entered by the user.***

Bot name:
```
@BotUserOpenWeatherBotBot
```

<p align="center"> 
  <img src="https://user-images.githubusercontent.com/43421023/133983926-af29c5a3-32f7-42c2-b0a0-5fb91ffa8a6b.png" alt="OpenWeatherBot">
</p>


## Used 

[![Python](https://img.shields.io/static/v1?label=Python&message=v3.9.4&color=00CC11)](https://www.python.org/downloads/release/python-394/)
[![Aiogram](https://img.shields.io/static/v1?label=Aiogram&message=v2.12.1&color=D75627)](https://docs.aiogram.dev/en/latest/)

API:
- [Open Weather API](https://openweathermap.org/api)


## Install 

- Install: [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

For project deployment:

Add Keys:
```sh
source setenv.sh
```
Docker Build:
```sh
docker build --no-cache --build-arg BOT_TOKEN=$BOT_TOKEN --build-arg OPEN_WEATHER_KEY=$OPEN_WEATHER_KEY -t owbot .
```
Docker Run:
```sh
docker run -i -t -p 80:80 owbot
```
