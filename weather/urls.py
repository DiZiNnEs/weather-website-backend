from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.__weather_all, name='all'),
    path('about/', views.about, name='about'),
    path('coordinates/', views.get_user_coordinates, name='get_user_coordinates'),
]
