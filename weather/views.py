from django.shortcuts import render
from .parser import (
    current_weather,
    forecast_daily,
)


async def index(request):
    weather_current_results: dict = current_weather()
    results = {
        # currently:
        'Clouds': weather_current_results['Clouds'],
        'Humidity': weather_current_results['Humidity'],
        'Status': weather_current_results['Status'],
        'Detailed_status': weather_current_results['Detailed_status'],
        'Visibility_distance': weather_current_results['Visibility_distance'],
        'Temperature': weather_current_results['Temperature'],
        'Weather_icon_name': weather_current_results['Weather_icon_name'],
    }

    return render(request, 'weather/index.html', results)


async def forecast_weekly(request):
    weather_forecast = forecast_daily()
    results_list = []

    for x in range(0, 7):
        results = {
            # weekly
            'Clouds_forecast': weather_forecast[x]['Clouds'],
            'Humidity_forecast': weather_forecast[x]['Humidity'],
            'Status_forecast': weather_forecast[x]['Status'],
            'Detailed_status_forecast': weather_forecast[x]['Detailed status'],
            'Visibility_distance_forecast': weather_forecast[x]['Visibility distance'],
            'Temperature_forecast': weather_forecast[x]['Temperature'],
            'Weather_icon_name_forecast': weather_forecast[x]['Weather_icon_name'],
        }
        results_list.append(results)

    return render(request, 'weather/weekly_forecast.html', results_list)
