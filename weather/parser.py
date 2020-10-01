from aiohttp import ClientSession
from asyncio import get_event_loop

from dotenv import load_dotenv

from typing import (
    Dict,
    Coroutine,
    Any,
)

import os

API_KEY = os.getenv('WEATHER_API_KEY')
