from django.db import models
from gestion_voluntarios.model.voluntario_model import Voluntario


class Emergencia(models.Model):
    nombre = models.CharField(max_length=50, default='')
    # Estado que define si la emergencia fue o no atendida
    esAtendida = models.BooleanField(default=False)
    voluntarios = models.ManyToManyField(Voluntario)

    def __int__(self, nombre, esAtendida, voluntarios):
        self.nombre = nombre
        self.esAtendida = esAtendida
        self.voluntarios = voluntarios

    def obtener_esAtendida(self, estado):
        self.esAtendida = estado