from django.urls import path

from . import views

urlpatterns = [
    path('current/', views.index, name='index'),
    path('weekly/', views.forecast_weekly, name='weekly'),
]
