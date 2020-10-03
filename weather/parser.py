from typing import (
    List,
    Dict,
)

from weather_website.env import env

from pyowm import OWM

API_KEY = env('WEATHER_API_KEY')
user_agent = {
    'User-Agent': env('USER_AGENT')
}

owm = OWM(API_KEY)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=52.5244, lon=13.4105)


def current_weather() -> Dict:
    return {
        'Clouds': one_call.current.clouds,
        'Humidity': one_call.current.humidity,
        'Status': one_call.current.status,
        'Detailed_status': one_call.current.detailed_status,
        'Visibility_distance': one_call.current.visibility_distance,
        'Temperature': one_call.current.temp,
        'Weather_icon_name': one_call.current.weather_icon_name,
    }


def forecast_daily() -> List:
    weather = []
    day = 1
    for x in range(0, 7):
        weather_dict = {
            'Clouds': one_call.forecast_daily[x].clouds,
            'Humidity': one_call.forecast_daily[x].humidity,
            'Status': one_call.forecast_daily[x].status,
            'Detailed status': one_call.forecast_daily[x].detailed_status,
            'Visibility distance': one_call.forecast_daily[x].visibility_distance,
            'Temperature': one_call.forecast_daily[x].temperature().get("day", None),
            'Weather_icon_name': one_call.forecast_daily[x].weather_icon_name,
        }
        day += 1
        weather.append(weather_dict)

    return weather


print(current_weather())
