from django.shortcuts import render
from .parser import handle_json


async def index(request):
    results = await handle_json()
    # print(results)
    city_weather = {
        'data': results['dt'],
        'sunset': results['sunset'],
        'temp': results['temp'],
    }
    print(city_weather['temp'])
    return render(request, 'weather/index.html')
