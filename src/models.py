"""
models.py - Module for defining the business logic of the project.
"""
import os
import json
import requests

# OpenWeather api key
API_KEY = os.getenv('OPEN_WEATHER_KEY')


class OpenWeather:

    def __init__(self):
        self.json_data = {}

    def get_request(self, name: str) -> None:
        """Main request to OpenWeather Api.
        At the input, it takes a string (name of a country or city),
        get json with a weather forecast or 404.
        """
        api_url = (
            'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            .format(name, API_KEY)
        )
        response = requests.get(api_url)
        self.json_data.update(response.json())

    def weather(self) -> dict[str, str]:
        icon = self.json_data['weather'][0]['icon'] + '.png'
        name = self.json_data['name']
        temp = self.json_data['main']['temp']
        description = self.json_data['weather'][0]['description']

        msg = f'{name}\n* temp: {temp}°f\n* {description}'
        return {'icon': icon, 'main': msg}

    def weather_item(self, arg: str) -> str:
        json_items = []
        name = self.json_data['name']

        for key, value in self.json_data[arg].items():
            json_items.append(f'* {key}: {value}\n')

        mkitem_str = ''.join(json_items)
        items = f'{name}\n{mkitem_str}'
        return items

    def error_msg(self) -> dict[str, str]:
        error_icon = 'error_404.jpg'
        error_msg = self.json_data['message'] + '\nEnter: /help'

        return {'error_icon': error_icon, 'error_msg': error_msg}

    def main_request(self, name: str) -> dict:
        self.get_request(name)

        if self.json_data['cod'] == '404':
            return self.error_msg()
        else:
            return self.weather()
