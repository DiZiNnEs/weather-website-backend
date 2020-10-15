from typing import (
    Dict,
    List,
)

from pyowm import OWM

from weather_website.env import env

API_KEY = env('WEATHER_API_KEY')
user_agent = {
    'User-Agent': env('USER_AGENT')
}

owm = OWM(API_KEY)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=52.5244, lon=13.4105)


def weather(weather_: str) -> Dict or List:
    weather_list = []
    day = 1
    if weather_ == 'current':
        return {
            'Clouds': one_call.current.clouds,
            'Humidity': one_call.current.humidity,
            'Status': one_call.current.status,
            'Detailed_status': one_call.current.detailed_status,
            'Visibility_distance': one_call.current.visibility_distance,
            'Temperature': one_call.current.temp.get('temp', None),
            'Weather_icon_name': one_call.current.weather_icon_name,
        }

    elif weather_ == 'minute':
        for x in range(0, 7):
            weather_dict = {
                'Clouds': one_call.forecast_minutely[x].clouds,
                'Humidity': one_call.forecast_minutely[x].humidity,
                'Status': one_call.forecast_minutely[x].status,
                'Detailed status': one_call.forecast_minutely[x].detailed_status,
                'Visibility distance': one_call.forecast_minutely[x].visibility_distance,
                'Temperature': one_call.forecast_minutely[x].temperature().get("day", None),
                'Weather_icon_name': one_call.forecast_minutely[x].weather_icon_name,
            }
            day += 1
            weather_list.append(weather_dict)

    elif weather_ == 'hourly':
        for x in range(0, 7):
            weather_dict = {
                'Clouds': one_call.forecast_hourly[x].clouds,
                'Humidity': one_call.forecast_hourly[x].humidity,
                'Status': one_call.forecast_hourly[x].status,
                'Detailed status': one_call.forecast_hourly[x].detailed_status,
                'Visibility distance': one_call.forecast_hourly[x].visibility_distance,
                'Temperature': one_call.forecast_hourly[x].temperature().get("day", None),
                'Weather_icon_name': one_call.forecast_hourly[x].weather_icon_name,
            }
            day += 1
            weather_list.append(weather_dict)

    elif weather_ == 'daily':
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
            weather_list.append(weather_dict)

    elif weather_ == 'weekly':
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
            weather_list.append(weather_dict)

    return weather_list


def weather_all():
    weather_list = []
    for x in range(0, 7):
        weather_dict = {
            'Clouds_daily': one_call.forecast_daily[x].clouds,
            'Humidity_daily': one_call.forecast_daily[x].humidity,
            'Status_daily': one_call.forecast_daily[x].status,
            'Detailed status_daily': one_call.forecast_daily[x].detailed_status,
            'Visibility distance_daily': one_call.forecast_daily[x].visibility_distance,
            'Temperature_daily': one_call.forecast_daily[x].temperature().get("day", None),
            'Weather_icon_name_daily': one_call.forecast_daily[x].weather_icon_name,

            'Clouds_hourly': one_call.forecast_hourly[x].clouds,
            'Humidity_hourly': one_call.forecast_hourly[x].humidity,
            'Status_hourly': one_call.forecast_hourly[x].status,
            'Detailed status_hourly': one_call.forecast_hourly[x].detailed_status,
            'Visibility distance_hourly': one_call.forecast_hourly[x].visibility_distance,
            'Temperature_hourly': one_call.forecast_hourly[x].temperature().get("day", None),
            'Weather_icon_name_hourly': one_call.forecast_hourly[x].weather_icon_name,

            'Clouds_minutely': one_call.forecast_minutely[x].clouds,
            'Humidity_minutely': one_call.forecast_minutely[x].humidity,
            'Status_minutely': one_call.forecast_minutely[x].status,
            'Detailed status_minutely': one_call.forecast_minutely[x].detailed_status,
            'Visibility distance_minutely': one_call.forecast_minutely[x].visibility_distance,
            'Temperature_minutely': one_call.forecast_minutely[x].temperature().get("day", None),
            'Weather_icon_name_minutely': one_call.forecast_minutely[x].weather_icon_name,
        }
        weather_list.append(weather_dict)

    return weather_list
