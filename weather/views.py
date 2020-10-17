from django.shortcuts import render

from .web.api_call import weather_all, weather_all
from .forms import CityForm

from .web import geoapi


async def index(request):
    weather_current_results: dict = weather_all('current')
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


def weather(request):
    call_weather = weather_all()
    results_list = []
    for x in range(0, 7):
        results = {
            'Clouds_daily': call_weather[x]['Clouds_daily'],
            'Humidity_daily': call_weather[x]['Humidity_daily'],
            'Status_daily': call_weather[x]['Status_daily'],
            'Detailed_status_daily': call_weather[x]['Detailed status_daily'],
            'Visibility_distance_forecast_daily': call_weather[x]['Visibility distance_daily'],
            'Temperature_forecast_daily': call_weather[x]['Temperature_daily'],
            'Weather_icon_name_forecast_daily': call_weather[x]['Weather_icon_name_daily'],

            'Clouds_hourly': call_weather[x]['Clouds_hourly'],
            'Humidity_hourly': call_weather[x]['Humidity_hourly'],
            'Status_hourly': call_weather[x]['Status_hourly'],
            'Detailed_status_hourly': call_weather[x]['Detailed status_hourly'],
            'Visibility_distance_forecast_hourly': call_weather[x]['Visibility distance_hourly'],
            'Temperature_forecast_hourly': call_weather[x]['Temperature_hourly'],
            'Weather_icon_name_forecast_hourly': call_weather[x]['Weather_icon_name_hourly'],

            'Clouds_minutely': call_weather[x]['Clouds_minutely'],
            'Humidity_minutely': call_weather[x]['Humidity_minutely'],
            'Status_minutely': call_weather[x]['Status_minutely'],
            'Detailed_status_minutely': call_weather[x]['Detailed status_minutely'],
            'Visibility_distance_forecast_minutely': call_weather[x]['Visibility distance_minutely'],
            'Temperature_forecast_minutely': call_weather[x]['Temperature_minutely'],
            'Weather_icon_name_forecast_minutely': call_weather[x]['Weather_icon_name_minutely'],
        }
        results_list.append(results)
    context = {'city_weather': results_list}

    return render(request, 'weather/weather.html', context)
