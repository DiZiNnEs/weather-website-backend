from django.shortcuts import render
from .parser import current_weather


async def index(request):
    results = await current_weather()
    # print(results)
    current_weather = {
        'data': results['dt'],
        'sunset': results['sunset'],
        'temp': results['temp'],
    }
    print(current_weather)
    return render(request, 'weather/index.html', current_weather)
