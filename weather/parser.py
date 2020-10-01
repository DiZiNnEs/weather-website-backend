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


async def request(lat: int, lon: int) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=weekly&appid={API_KEY}'
    session = ClientSession()
    async with session.get(url=url, headers=user_agent) as response_from_server:
        content = await response_from_server.json()
    await session.close()

    return content


async def current_weather() -> dict:
    result = await request(31, 32)
    return {
        'current':
            {
                'data': result['dt'],
                'sunrise': result['sunrise'],
                'temp': result['temp'],
                'fells like': result['fells_like'],
                'humidity': result['humidity'],
                'dew point': result['dew_point '],
                'uvi': result['uvi'],
                'clouds': result['clouds'],
                'visibility': result['visibility'],
                'wind speed': result['wind_speed'],
                'wind deg': result['wind_deg'],
                'weather': {
                    'id': result['id'],
                    "main": result['Clouds'],
                    "description": result['broken clouds'],
                    "icon": result['04n']
                }
            }
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
