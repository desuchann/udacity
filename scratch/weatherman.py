import requests
import datetime as dt


class WeatherService:

    def getForecast(city, country):
        appId = 'c9e4da4de1eccd93eec9c6c228501c9c'
        # available in json or xml mode
        baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
        response = requests.get(baseUrl, params=[(
            'q', f'{city},{country}'), ('appid', appId), ('mode', 'json')])
        data = response.json()
        return data['list']


def umbrella(city, country, day=None):
    chances = False
    day = dt.date(2021, 10, day) if day else dt.date.today()
    data = WeatherService.getForecast(city, country)
    today = [x for x in data if dt.datetime.strptime(
        x['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == day]
    rain = [x.get('rain')['3h'] for x in today if x.get('rain')]
    if rain and any(x > 0.3 for x in rain):
        chances = True
    return chances


if __name__ == "__main__":
    umbrella('London', 'UK', 3)
