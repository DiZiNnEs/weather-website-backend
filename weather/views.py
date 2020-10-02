from django.shortcuts import render
from .parser import


async def index(request):

    return render(request, 'weather/index.html', ...)
