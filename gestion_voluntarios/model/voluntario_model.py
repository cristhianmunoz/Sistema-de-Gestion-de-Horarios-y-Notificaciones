import django
from django.db import models
from django.db import connection

from gestion_voluntarios.model.emergencia_model import Emergencia

#django.setup()


class Voluntario(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default='')
    nombre = models.CharField(max_length=50, default='')
    es_asignado = models.BooleanField(default=False)
    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE, related_name='voluntarios')

    def get_es_asignado(self):
        return self.es_asignado

    def __str__(self):
        return f'Voluntario: {self.nombre}, {self.es_asignado}'
