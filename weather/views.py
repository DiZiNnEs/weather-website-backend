from django.shortcuts import render

from .web.api_call import weather, weather_all
from .forms import CityForm

from .web import geoapi


async def index(request):
    weather_current_results: dict = weather('current')
    form = CityForm()

    results = {
        # currently:
        'Clouds': weather_current_results['Clouds'],
        'Humidity': weather_current_results['Humidity'],
        'Status': weather_current_results['Status'],
        'Detailed_status': weather_current_results['Detailed_status'],
        'Visibility_distance': weather_current_results['Visibility_distance'],
        'Temperature': weather_current_results['Temperature'],
        'Weather_icon_name': weather_current_results['Weather_icon_name'],
        'form': form,
    }

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'weather/index.html', results)


def get_user_coordinates(request):
    form = CityForm()
    lan_and_lon = ''

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('name'))
        lan_and_lon = geoapi.get_coordinates(request.POST.get('name'))

    results_to_templates = {
        'form': form,
        'lan_and_lon': lan_and_lon
    }

    return render(request, 'weather/get_user_coordinates.html', results_to_templates)


def about(request):
    return render(request, 'weather/about.html')


def __weather_all(request):
    weather = weather_all()
    results_list = []
    for x in range(0, 7):
        results = {
            'Clouds_daily': weather[x]['Clouds_daily'],
            'Humidity_daily': weather[x]['Humidity_daily'],
            'Status_daily': weather[x]['Status_daily'],
            'Detailed_status_daily': weather[x]['Detailed status_daily'],
            'Visibility_distance_forecast_daily': weather[x]['Visibility distance_daily'],
            'Temperature_forecast_daily': weather[x]['Temperature_daily'],
            'Weather_icon_name_forecast_daily': weather[x]['Weather_icon_name_daily'],

            'Clouds_hourly': weather[x]['Clouds_hourly'],
            'Humidity_hourly': weather[x]['Humidity_hourly'],
            'Status_hourly': weather[x]['Status_hourly'],
            'Detailed_status_hourly': weather[x]['Detailed status_hourly'],
            'Visibility_distance_forecast_hourly': weather[x]['Visibility distance_hourly'],
            'Temperature_forecast_hourly': weather[x]['Temperature_hourly'],
            'Weather_icon_name_forecast_hourly': weather[x]['Weather_icon_name_hourly'],

            'Clouds_minutely': weather[x]['Clouds_minutely'],
            'Humidity_minutely': weather[x]['Humidity_minutely'],
            'Status_minutely': weather[x]['Status_minutely'],
            'Detailed_status_minutely': weather[x]['Detailed status_minutely'],
            'Visibility_distance_forecast_minutely': weather[x]['Visibility distance_minutely'],
            'Temperature_forecast_minutely': weather[x]['Temperature_minutely'],
            'Weather_icon_name_forecast_minutely': weather[x]['Weather_icon_name_minutely'],
        }
        results_list.append(results)
    context = {'city_weather': results_list}

    return render(request, 'weather/weather.html', context)
