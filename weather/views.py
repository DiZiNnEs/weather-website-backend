from django.shortcuts import render
from .parser import current_weather


async def index(request):
    weather_results: dict = current_weather()
    results = {
        'Clouds': weather_results['Clouds'],
        'Humidity': weather_results['Humidity'],
        'Status': weather_results['Status'],
        'Detailed_status': weather_results['Detailed_status'],
        'Visibility_distance': weather_results['Visibility_distance'],
        'Temperature': weather_results['Temperature'],
        'Weather_icon_name': weather_results['Weather_icon_name'],
    }
    return render(request, 'weather/index.html', results)
