from aiohttp import ClientSession
from asyncio import get_event_loop

from weather_website.env import env

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

API_KEY = env('WEATHER_API_KEY')
user_agent = {
    'User-Agent': env('USER_AGENT')
}

owm = OWM(API_KEY)
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=52.5244, lon=13.4105)


def current_weather():
    return {
        'Clouds': one_call.current.clouds,
        'Humidity': one_call.current.humidity,
        'Status': one_call.current.status,
        'Detailed status': one_call.current.detailed_status,
        'Visibility distance': one_call.current.visibility_distance,
        'Temperature': one_call.current.temp
    }


print(current_weather())

# if __name__ == '__main__':
#     loop = get_event_loop()
#     loop.run_until_complete(test())
