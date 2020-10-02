from django.shortcuts import render
from .parser import current_weather


async def index(request):
    current = current_weather()
    print()
    return render(request, 'weather/index.html', current_weather())
