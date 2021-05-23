import os
import json
import requests

from utils import StaticData

API_KEY = os.getenv('OPEN_WEATHER_KEY')


class OpenWeather(StaticData):

    def __init__(self):
        self.json_data = {}

    def get_request(self, name):
        """
        Main request to OpenWeather Api.
        """
        api_url = (
            'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            .format(name, API_KEY)
        )
        response = requests.get(api_url)
        self.json_data.update(response.json())

    def main_request(self, name) -> list:
        """docstring for clean_data"""
        self.get_request(name)

        if self.json_data['cod'] == '404':
            return self.error_msg()
        else:
            return self.weather()

    def weather(self) -> list:
        """docstring for weather"""
        get_icon = self.json_data['weather'][0]['icon']
        icon = self.take_img(f'{get_icon}.png')
        name = self.json_data['name']
        tsmp = self.json_data['main']['temp']
        description = self.json_data['weather'][0]['description']
        items = f'{name}\ntemp: {tsmp}\n{description}'
        return icon, items

    def error_msg(self):
        icon = self.take_img('error_404.jpg')
        msg = self.json_data['message']
        return icon, msg

    def weather_item(self, arg) -> str:
        json_items = []
        for key, value in self.json_data[arg].items():
            json_items.append(f"* {key}: {value}\n")
        mkstr = ''.join(json_items)
        return mkstr

if __name__=='__main__':
    W = OpenWeather()
    print(W.main_request('Tbilisi'))
    print(W.weather_items('main'))
    print(W.weather_items('clouds'))
    print(W.weather_items('sys'))
    print(W.weather_items('coord'))
