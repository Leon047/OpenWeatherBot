import os
import json
import requests

from utils import StaticData

API_KEY = os.getenv('OPEN_WEATHER_KEY')
static = os.path.abspath('static/img/')


class OpenWeather(StaticData):

    def __init__(self) -> None:
        self.json_data = {}

    def get_request(self, name) -> None:
        """
        Main request to OpenWeather Api.
        """
        api_url = (
            'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            .format(name, API_KEY)
        )
        response = requests.get(api_url)
        self.json_data.update(response.json())

    def main_response(self, name) -> list:
        """docstring for clean_data"""
        self.get_request(name)

        if self.json_data['cod'] == '404':
            return self.json_data['message']
        else:
            return self.weather()

    def weather(self) -> list:
        """docstring for weather"""
        icon = self.json_data['weather'][0]['icon']
        img = self.take_img(f'{icon}.png')

        name = self.json_data['name']
        tsmp = self.json_data['main']['temp']
        description = self.json_data['weather'][0]['description']

        items = f'{name}\ntemp: {tsmp}\n{description}'
        return img, items

    def main(self) -> dict:
        """docstring for main"""
        return self.json_data['main']

    def visibility(self) -> dict:
        """docstring for visibility"""
        return self.json_data['visibility']

    def clouds(self) -> dict:
        """docstring for clouds"""
        return self.json_data['clouds']

    def sys(self) -> dict:
        """docstring for sys"""
        return self.json_data['sys']

    def coord(self) -> dict:
        """docstring for coord"""
        return self.json_data['coord']

if __name__=='__main__':
    M = OpenWeather()
    M.take_response('Tbilisi')
