from django.shortcuts import render
from .parser import current_weather


async def index(request):
    results = await current_weather()
    # print(results)
    test = {
        'temp': results['temp']
    }
    return render(request, 'weather/index.html', test)
