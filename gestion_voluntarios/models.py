from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=20, default='')
    apellido = models.CharField(max_length=20, default='')
    edad = models.IntegerField(default=0)

