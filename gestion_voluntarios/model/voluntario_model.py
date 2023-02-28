from django.db import models

from common.model.horario_model import Horario
from gestion_voluntarios.model.habilidad_model import Habilidad


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)

    # Estado que define si tiene o no una actividad asignada
    tieneActividad = models.BooleanField(default=False)

    # No utilizamos para las actividades
    habilidades = models.ManyToManyField(Habilidad)
    horarioDisponible = models.OneToOneField(Horario, on_delete=models.CASCADE)

    def __int__(self, nombre, apellido, edad, tieneActividad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tieneActividad = tieneActividad

    def comprobarDisponibilidad(self):
        pass
