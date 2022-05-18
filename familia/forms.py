import datetime
from email.utils import format_datetime
from wsgiref.handlers import format_date_time
from xmlrpc.client import _datetime_type
from django import forms
from numpy import datetime_data

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    DNI = forms.IntegerField(label="DNI")
    nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats = ["%d/%m/%Y"],
    
    widget=forms.TextInput(attrs={'placeholder': '30/08/1985'}))