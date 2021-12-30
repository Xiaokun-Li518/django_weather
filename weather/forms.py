from django import forms
from django.forms import ModelForm, TextInput, fields, widgets

from .models import City 

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder':'City Name'})
        }



class CityFormNotModel(forms.Form):
    name = forms.CharField(max_length=25)       
    widgets =  {
            'name': TextInput(attrs={'class': 'input', 'placeholder':'City Name'})
        }