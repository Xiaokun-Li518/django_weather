
from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.shortcuts import render
from django.urls.base import reverse 
import requests

from django.http import HttpResponseRedirect

from .models import City

from .forms import CityForm, CityFormNotModel

from django.views.generic.edit import CreateView, UpdateView, DeleteView 

from django.urls import reverse_lazy


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=95884f62299ee675da8b659b8c37d21d'
    cities = City.objects.all()
    print(cities)


    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']
            if not City.objects.filter(name=city):
                form.save()
    else:
        form = CityForm()


    
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json() # request the API data and convert the JSON to Python data types
        weather = {
            'city':city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }
        weather_data.append(weather)


    context = {
        'weather_data': weather_data,
        'form': form,
    }


    return render(request, 'weather/index.html', context)





     