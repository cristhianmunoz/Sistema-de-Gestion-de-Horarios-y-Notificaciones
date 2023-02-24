from datetime import datetime
from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=20, default='')
    apellido = models.CharField(max_length=20, default='')
    edad = models.IntegerField(default=0)


class Emergencia(models.Model):
    asunto = models.CharField(max_length=50, default='')
    tipo_emergencia = models.CharField(max_length=20, default='')
    ubicacion = models.CharField(max_length=200, default='')
    # recursos = models.CharField(max_length=200, default='')
    hora_entrada = models.DateTimeField(default=datetime.now())
    encargado = models.CharField(max_length=20, default='')
    dirigido_a = models.CharField(max_length=500, default='Ninguno')
    actividades = models.CharField(max_length=500, null=False)
    detalle = models.CharField(max_length=500, default='Ninguno')

