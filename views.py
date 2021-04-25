import os
import requests

OPEN_WEATHER_API = os.getenv('OPEN_WEATHER_KEY')
API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

def openweather_api_requst(city_or_country):
    """Request to OpenWeather Api and get json response."""
    api_url = (
        'https://api.openweathermap.org/data/2.5/weather?q={}&mode=html&appid={}'
               .format(city_or_country, API_KEY)
    )
    api_response = requests.get(api_url)
    return api_response

def take_data(arg='London'):
    data = openweather_api_requst(arg)
    print(data)

    # try:
    #     data = openweather_api_requst(arg)
    # except:
    #     print('Введите страну, город или регион.')

if __name__=='__main__':
    take_data()
