from django.shortcuts import render

from .web.api_call import weather_all, weather_current
from .forms import CityForm

from .web import geoapi


async def index(request):
    weather_current_results: dict = weather_current()

    results = {
        'Clouds': weather_current_results['Clouds'],
        'Dewpoint': weather_current_results['Dewpoint'],
        'Heat_index': weather_current_results['Heat_index'],
        'humidex': weather_current_results['humidex'],
        'Humidity': weather_current_results['Humidity'],
        'Pressure': weather_current_results['Pressure'],
        'Rain': weather_current_results['Rain'],
        'Ref_time': weather_current_results['Ref_time'],
        'Snow': weather_current_results['Snow'],
        'Srise_time': weather_current_results['Srise_time'],
        'sset_time': weather_current_results['sset_time'],
        'Status': weather_current_results['Status'],
        'Detailed_status': weather_current_results['Detailed_status'],
        'Visibility_distance': weather_current_results['Visibility_distance'],
        'Temperature': weather_current_results['Temperature'],
        'Utc_offset': weather_current_results['Utc_offset'],
        'Uvi': weather_current_results['Uvi'],
        'Wind': weather_current_results['Wind'],
        'Weather_icon_name': weather_current_results['Weather_icon_name'],
    }

    return render(request, 'weather/index.html', results)


def weather(request):
    call_weather = weather_all()
    results_list = []
    for get_weather_information in range(0, 7):
        results = {
            'Clouds_daily': call_weather[get_weather_information]['Clouds_daily'],
            'Humidity_daily': call_weather[get_weather_information]['Humidity_daily'],
            'Status_daily': call_weather[get_weather_information]['Status_daily'],
            'Detailed_status_daily': call_weather[get_weather_information]['Detailed status_daily'],
            'Visibility_distance_forecast_daily': call_weather[get_weather_information]['Visibility distance_daily'],
            'Temperature_forecast_daily': call_weather[get_weather_information]['Temperature_daily'],
            'Weather_icon_name_forecast_daily': call_weather[get_weather_information]['Weather_icon_name_daily'],
            #  new daily
            'Heat_index_daily': call_weather[get_weather_information]['Heat_index_daily'],
            'Pressure_daily': call_weather[get_weather_information]['Pressure_daily'],
            'Rain_daily': call_weather[get_weather_information]['Rain_daily'],
            'Ref_time_daily': call_weather[get_weather_information]['Ref_time_daily'],
            'Snow_daily': call_weather[get_weather_information]['Snow_daily'],
            'Srise_time_daily': call_weather[get_weather_information]['Srise_time_daily'],
            'sset_time_daily': call_weather[get_weather_information]['sset_time_daily'],
            'Utc_offset_daily': call_weather[get_weather_information]['Utc_offset_daily'],
            'Uvi_daily': call_weather[get_weather_information]['Uvi_daily'],
            'Detailed status_daily': call_weather[get_weather_information]['Detailed status_daily'],
            'Visibility distance_daily': call_weather[get_weather_information]['Visibility distance_daily'],
            'Temperature_daily': call_weather[get_weather_information]['Temperature_daily'],
            'Wind_daily': call_weather[get_weather_information]['Wind_daily'],


            'Clouds_hourly': call_weather[get_weather_information]['Clouds_hourly'],
            'Humidity_hourly': call_weather[get_weather_information]['Humidity_hourly'],
            'Status_hourly': call_weather[get_weather_information]['Status_hourly'],
            'Detailed_status_hourly': call_weather[get_weather_information]['Detailed status_hourly'],
            'Visibility_distance_forecast_hourly': call_weather[get_weather_information]['Visibility distance_hourly'],
            'Temperature_forecast_hourly': call_weather[get_weather_information]['Temperature_hourly'],
            'Weather_icon_name_forecast_hourly': call_weather[get_weather_information]['Weather_icon_name_hourly'],
            #  new hourly
            'Heat_index_hourly': call_weather[get_weather_information]['Heat_index_hourly'],
            'Pressure_hourly': call_weather[get_weather_information]['Pressure_hourly'],
            'Rain_hourly': call_weather[get_weather_information]['Rain_hourly'],
            'Ref_time_hourly': call_weather[get_weather_information]['Ref_time_hourly'],
            'Snow_hourly': call_weather[get_weather_information]['Snow_hourly'],
            'Srise_time_hourly': call_weather[get_weather_information]['Srise_time_hourly'],
            'sset_time_hourly': call_weather[get_weather_information]['sset_time_hourly'],
            'Utc_offset_hourly': call_weather[get_weather_information]['Utc_offset_hourly'],
            'Uvi_hourly': call_weather[get_weather_information]['Uvi_hourly'],
            'Detailed status_hourly': call_weather[get_weather_information]['Detailed status_hourly'],
            'Visibility distance_hourly': call_weather[get_weather_information]['Visibility distance_hourly'],
            'Temperature_hourly': call_weather[get_weather_information]['Temperature_hourly'],
            'Wind_hourly': call_weather[get_weather_information]['Wind_hourly'],


            'Clouds_minutely': call_weather[get_weather_information]['Clouds_minutely'],
            'Humidity_minutely': call_weather[get_weather_information]['Humidity_minutely'],
            'Status_minutely': call_weather[get_weather_information]['Status_minutely'],
            'Detailed_status_minutely': call_weather[get_weather_information]['Detailed status_minutely'],
            'Visibility_distance_forecast_minutely': call_weather[get_weather_information][
                'Visibility distance_minutely'],
            'Temperature_forecast_minutely': call_weather[get_weather_information]['Temperature_minutely'],
            'Weather_icon_name_forecast_minutely': call_weather[get_weather_information]['Weather_icon_name_minutely'],
            #  new minutely
            'Heat_index_minutely': call_weather[get_weather_information]['Heat_index_minutely'],
            'Pressure_minutely': call_weather[get_weather_information]['Pressure_minutely'],
            'Rain_minutely': call_weather[get_weather_information]['Rain_minutely'],
            'Ref_time_minutely': call_weather[get_weather_information]['Ref_time_minutely'],
            'Snow_minutely': call_weather[get_weather_information]['Snow_minutely'],
            'Srise_time_minutely': call_weather[get_weather_information]['Srise_time_minutely'],
            'sset_time_minutely': call_weather[get_weather_information]['sset_time_minutely'],
            'Utc_offset_minutely': call_weather[get_weather_information]['Utc_offset_minutely'],
            'Uvi_minutely': call_weather[get_weather_information]['Uvi_minutely'],
            'Detailed status_minutely': call_weather[get_weather_information]['Detailed status_minutely'],
            'Visibility distance_minutely': call_weather[get_weather_information]['Visibility distance_minutely'],
            'Temperature_minutely': call_weather[get_weather_information]['Temperature_minutely'],
            'Wind_minutely': call_weather[get_weather_information]['Wind_minutely'],
        }
        results_list.append(results)
    context = {'city_weather': results_list}

    return render(request, 'weather/weather.html', context)


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
