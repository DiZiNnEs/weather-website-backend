from typing import (
    Dict,
)

from pyowm import OWM

from weather_website.env import env

API_KEY = env('WEATHER_API_KEY')
user_agent = {
    'User-Agent': env('USER_AGENT')
}

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_coordinates(city: str) -> Dict[str, float]:
    request = mgr.weather_at_place(city)
    return {'lat': request.location.lat,
            'lon': request.location.lon}


print(get_coordinates('Kokshetau'))
