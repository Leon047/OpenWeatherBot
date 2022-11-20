# OpenWeatherBot

> Demo telegram bot


## Description 

> Telegram bot that allows you to find out the weather of a certain location, the name of which will be entered.

Bot name:
```
@BotUserOpenWeatherBotBot
```

<p align="center"> 
  <img src="https://user-images.githubusercontent.com/43421023/133983926-af29c5a3-32f7-42c2-b0a0-5fb91ffa8a6b.png" alt="OpenWeatherBot">
</p>


## Used 

[![Python](https://img.shields.io/static/v1?label=Python&message=v3.9.4&color=007DD1)](https://www.python.org/downloads/release/python-394/)
[![Aiogram](https://img.shields.io/static/v1?label=Aiogram&message=v2.12.1&color=007DD1)](https://docs.aiogram.dev/en/latest/)

API:
- [Open Weather API](https://openweathermap.org/api)


## Install 

- Install: [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

For project deployment:

```sh
source setenv.sh
```
```sh
docker build --no-cache --build-arg BOT_TOKEN=$BOT_TOKEN --build-arg OPEN_WEATHER_KEY=$OPEN_WEATHER_KEY -t owbot .
```
```sh
docker run -i -t -p 80:80 owbot
'''

