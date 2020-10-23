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


def get_daily_weather(request):
    call_weather = weather_all()
    results_list = []
    for get_weather_information_daily in range(0, 8):
        results = {
            'Clouds_daily': call_weather[get_weather_information_daily]['Clouds_daily'],
            'Humidity_daily': call_weather[get_weather_information_daily]['Humidity_daily'],
            'Status_daily': call_weather[get_weather_information_daily]['Status_daily'],
            'Detailed_status_daily': call_weather[get_weather_information_daily]['Detailed status_daily'],
            'Visibility_distance_forecast_daily': call_weather[get_weather_information_daily][
                'Visibility distance_daily'],
            'Temperature_forecast_daily': call_weather[get_weather_information_daily]['Temperature_daily'],
            'Weather_icon_name_forecast_daily': call_weather[get_weather_information_daily]['Weather_icon_name_daily'],
            'Heat_index_daily': call_weather[get_weather_information_daily]['Heat_index_daily'],
            'Pressure_daily': call_weather[get_weather_information_daily]['Pressure_daily'],
            'Rain_daily': call_weather[get_weather_information_daily]['Rain_daily'],
            'Ref_time_daily': call_weather[get_weather_information_daily]['Ref_time_daily'],
            'Snow_daily': call_weather[get_weather_information_daily]['Snow_daily'],
            'Srise_time_daily': call_weather[get_weather_information_daily]['Srise_time_daily'],
            'sset_time_daily': call_weather[get_weather_information_daily]['sset_time_daily'],
            'Utc_offset_daily': call_weather[get_weather_information_daily]['Utc_offset_daily'],
            'Uvi_daily': call_weather[get_weather_information_daily]['Uvi_daily'],
            'Visibility_distance_daily': call_weather[get_weather_information_daily]['Visibility distance_daily'],
            'Temperature_daily': call_weather[get_weather_information_daily]['Temperature_daily'],
            'Wind_daily': call_weather[get_weather_information_daily]['Wind_daily'],
        }
        results_list.append(results)
        context = {'city_weather_daily': results_list}

        return render(request, 'weather/weather.html', context)


def get_hourly_weather(request):
    call_weather = weather_all()
    results_list = []
    for get_weather_information_hourly in range(19, 55):
        results = {
            'Clouds_hourly': call_weather[get_weather_information_hourly]['Clouds_hourly'],
            'Humidity_hourly': call_weather[get_weather_information_hourly]['Humidity_hourly'],
            'Status_hourly': call_weather[get_weather_information_hourly]['Status_hourly'],
            'Detailed_status_hourly': call_weather[get_weather_information_hourly]['Detailed status_hourly'],
            'Visibility_distance_forecast_hourly': call_weather[get_weather_information_hourly][
                'Visibility distance_hourly'],
            'Temperature_forecast_hourly': call_weather[get_weather_information_hourly]['Temperature_hourly'],
            'Weather_icon_name_forecast_hourly': call_weather[get_weather_information_hourly][
                'Weather_icon_name_hourly'],
            'Heat_index_hourly': call_weather[get_weather_information_hourly]['Heat_index_hourly'],
            'Pressure_hourly': call_weather[get_weather_information_hourly]['Pressure_hourly'],
            'Rain_hourly': call_weather[get_weather_information_hourly]['Rain_hourly'],
            'Ref_time_hourly': call_weather[get_weather_information_hourly]['Ref_time_hourly'],
            'Snow_hourly': call_weather[get_weather_information_hourly]['Snow_hourly'],
            'Srise_time_hourly': call_weather[get_weather_information_hourly]['Srise_time_hourly'],
            'sset_time_hourly': call_weather[get_weather_information_hourly]['sset_time_hourly'],
            'Utc_offset_hourly': call_weather[get_weather_information_hourly]['Utc_offset_hourly'],
            'Uvi_hourly': call_weather[get_weather_information_hourly]['Uvi_hourly'],
            'Visibility_distance_hourly': call_weather[get_weather_information_hourly][
                'Visibility distance_hourly'],
            'Temperature_hourly': call_weather[get_weather_information_hourly]['Temperature_hourly'],
            'Wind_hourly': call_weather[get_weather_information_hourly]['Wind_hourly'],
        }
        results_list.append(results)

    context = {'city_weather_hourly': results_list}

    return render(request, 'weather/weather.html', context)
