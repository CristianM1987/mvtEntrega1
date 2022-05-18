import datetime
from wsgiref.handlers import format_date_time
from django.db import models
from numpy import datetime_data

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dni = models.IntegerField()
    nacimiento = models.DateField()
