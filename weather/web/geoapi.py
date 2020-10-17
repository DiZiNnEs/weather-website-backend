from typing import (
    Dict,
)

from pyowm.commons.exceptions import NotFoundError
from pyowm import OWM

from weather_website.env import env

API_KEY = env('WEATHER_API_KEY')
user_agent = {
    'User-Agent': env('USER_AGENT')
}

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_coordinates(city: str) -> Dict[str, float] or str:
    try:
        request = mgr.weather_at_place(city)
        return {'lat': request.location.lat,
                'lon': request.location.lon}
    except NotFoundError:
        return 'Unable tp find the resource'
