from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weekly/', views.forecast_weekly, name='weekly'),
    path('hourly/', views.forecast_hourly, name='hourly'),
    path('minute/', views.forecast_minute, name='minute'),
]
