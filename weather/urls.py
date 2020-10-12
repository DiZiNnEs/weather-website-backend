from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weekly/', views.forecast_daily, name='weekly'),
    path('hourly/', views.forecast_hourly, name='hourly'),
    path('minute/', views.forecast_minute, name='minute'),
    path('about/', views.about, name='about'),
    path('coordinates/', views.get_user_coordinates, name='get_user_coordinates'),
]
