from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.get_daily_weather and views.get_hourly_weather, name='all_weather'),
    path('about/', views.about, name='about'),
    path('get_coordinates/', views.get_user_coordinates, name='get_user_coordinates'),
]
