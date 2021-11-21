import os
import json
import requests

from utils import StaticData

API_KEY = os.getenv('OPEN_WEATHER_KEY')


class OpenWeather(StaticData):

    def __init__(self):
        self.json_data = {}

    def get_request(self, name) -> None:
        """Main request to OpenWeather Api.
        At the input, it takes a string (name of a country or city),
        returns json with a weather forecast or 404.
        """
        api_url = (
            'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            .format(name, API_KEY)
        )
        response = requests.get(api_url)
        self.json_data.update(response.json())

    def weather(self) -> list:
        get_icon = self.json_data['weather'][0]['icon']
        icon = self.take_img(f'{get_icon}.png')
        name = self.json_data['name']
        tsmp = self.json_data['main']['temp']
        description = self.json_data['weather'][0]['description']
        items = f'{name}\n* temp: {tsmp}°f\n* {description}'
        return icon, items

    def weather_item(self, arg) -> str:
        json_items = []
        name = self.json_data['name']
        for key, value in self.json_data[arg].items():
            json_items.append(f'* {key}: {value}\n')
        mkitem_str = ''.join(json_items)
        items = f'{name}\n{mkitem_str}'
        return items

    def error_msg(self) -> list:
        error_icon = self.take_img('error_404.jpg')
        error_msg = self.json_data['message']
        error_msg = f'{error_msg}\nEnter: /help'
        return '404', error_icon, error_msg

    def main_request(self, name) -> list:
        self.get_request(name)
        if self.json_data['cod'] == '404':
            return self.error_msg()
        else:
            return self.weather()
