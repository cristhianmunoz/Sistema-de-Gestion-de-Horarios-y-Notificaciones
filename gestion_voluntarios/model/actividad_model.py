from django.db import models
from gestion_voluntarios.model.emergencia_model import Emergencia


class Actividad(models.Model):
    nombre = models.CharField(max_length=50, default='')
    emergencias = models.ManyToManyField(Emergencia)

    def __int__(self, nombre, emergencias):
        self.nombre = nombre
        self.emergencias = emergencias

    def asignarVoluntario(self):
        pass


