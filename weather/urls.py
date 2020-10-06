from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weekly/', views.forecast_weekly, name='weekly'),
]
