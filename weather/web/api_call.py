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

print()


def weather_current() -> Dict or List:
    return {
        'Clouds': one_call.current.clouds,
        'Detailed_status': one_call.current.detailed_status,
        'Dewpoint': one_call.current.dewpoint,
        'Heat_index': one_call.current.heat_index,
        'humidex': one_call.current.humidex,
        'Humidity': one_call.current.humidity,
        'Pressure': one_call.current.pressure,
        'Rain': one_call.current.rain,
        'Ref_time': one_call.current.ref_time,
        'Snow': one_call.current.snow,
        'Srise_time': one_call.current.srise_time,
        'sset_time': one_call.current.sset_time,
        'Status': one_call.current.status,
        'Temperature': one_call.current.temp.get('temp', None),
        'Utc_offset': one_call.current.utc_offset,
        'Uvi': one_call.current.uvi,
        'Visibility_distance': one_call.current.visibility_distance,
        'Wind': one_call.current.wind,
        'Weather_icon_name': one_call.current.weather_icon_name,
    }


def weather_all() -> Dict or List:
    weather_list = []

    for x in range(0, 8):
        weather_dict = {
            'Clouds_daily': one_call.forecast_daily[x].clouds,
            'Dewpoint_daily': one_call.forecast_daily[x].dewpoint,
            'Heat_index_daily': one_call.forecast_daily[x].heat_index,
            'humidex_daily': one_call.forecast_daily[x].humidex,
            'Pressure_daily': one_call.forecast_daily[x].pressure,
            'Rain_daily': one_call.forecast_daily[x].rain,
            'Ref_time_daily': one_call.forecast_daily[x].ref_time,
            'Snow_daily': one_call.forecast_daily[x].snow,
            'Srise_time_daily': one_call.forecast_daily[x].srise_time,
            'sset_time_daily': one_call.forecast_daily[x].sset_time,
            'Humidity_daily': one_call.forecast_daily[x].humidity,
            'Utc_offset_daily': one_call.forecast_daily[x].utc_offset,
            'Uvi_daily': one_call.forecast_daily[x].uvi,
            'Status_daily': one_call.forecast_daily[x].status,
            'Detailed status_daily': one_call.forecast_daily[x].detailed_status,
            'Visibility distance_daily': one_call.forecast_daily[x].visibility_distance,
            'Temperature_daily': one_call.forecast_daily[x].temperature().get("day", None),
            'Wind_daily': one_call.forecast_daily[x].wind,
            'Weather_icon_name_daily': one_call.forecast_daily[x].weather_icon_name,

        }
        weather_list.append(weather_dict)

    for get_weather_information_2 in range(0, 48):
        weather_dict = {
            'Clouds_hourly': one_call.forecast_hourly[get_weather_information_2].clouds,
            'Dewpoint_hourly': one_call.forecast_hourly[get_weather_information_2].dewpoint,
            'Heat_index_hourly': one_call.forecast_hourly[get_weather_information_2].heat_index,
            'humidex_hourly': one_call.forecast_hourly[get_weather_information_2].humidex,
            'Pressure_hourly': one_call.forecast_hourly[get_weather_information_2].pressure,
            'Rain_hourly': one_call.forecast_hourly[get_weather_information_2].rain,
            'Ref_time_hourly': one_call.forecast_hourly[get_weather_information_2].ref_time,
            'Snow_hourly': one_call.forecast_hourly[get_weather_information_2].snow,
            'Srise_time_hourly': one_call.forecast_hourly[get_weather_information_2].srise_time,
            'sset_time_hourly': one_call.forecast_hourly[get_weather_information_2].sset_time,
            'Humidity_hourly': one_call.forecast_hourly[get_weather_information_2].humidity,
            'Utc_offset_hourly': one_call.forecast_hourly[get_weather_information_2].utc_offset,
            'Uvi_hourly': one_call.forecast_hourly[get_weather_information_2].uvi,
            'Status_hourly': one_call.forecast_hourly[get_weather_information_2].status,
            'Detailed status_hourly': one_call.forecast_hourly[get_weather_information_2].detailed_status,
            'Visibility distance_hourly': one_call.forecast_hourly[get_weather_information_2].visibility_distance,
            'Temperature_hourly': one_call.forecast_hourly[get_weather_information_2].temperature().get("day", None),
            'Wind_hourly': one_call.forecast_hourly[get_weather_information_2].wind,
            'Weather_icon_name_hourly': one_call.forecast_hourly[get_weather_information_2].weather_icon_name,
        }
        weather_list.append(weather_dict)

    return weather_list
