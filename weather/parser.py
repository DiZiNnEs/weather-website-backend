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

def pyowm_parser() -> None:
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=52.5244, lon=13.4105)
    for x in one_call.forecast_daily:
        print(x)


pyowm_parser()
# if __name__ == '__main__':
#     loop = get_event_loop()
#     loop.run_until_complete(test())
