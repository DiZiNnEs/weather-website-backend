from django.shortcuts import render
from .parser import current_weather


async def index(request):
    weather_results: dict = current_weather()
    results = {
        'Clouds': weather_results['Clouds'],
        'Humidity': weather_results['Humidity'],
        'Status': weather_results['Status'],
        'Detailed status': weather_results['Detailed_status'],
        'Visibility distance': weather_results['Visibility_distance'],
        'Temperature': weather_results['Temperature'],

    }
    return render(request, 'weather/index.html', results)
