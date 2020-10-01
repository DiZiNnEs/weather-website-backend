from django.shortcuts import render
from .parser import handle_json


def index(request):
    return render(request, 'weather/index.html')
