import django
django.setup()
from django.db import models

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.voluntario_model import Voluntario


class Habilidad(models.Model):
    titulo = models.CharField(choices=HabilidadMedica.choices)
    descripcion = models.CharField(max_length=200, default='')
    horasExperiencia = models.PositiveIntegerField(default=0)
    voluntario = Voluntario()

    def __init__(self, voluntario, titulo, horasExperiencia):
        self.voluntario = voluntario
        self.titulo = titulo
        self.horasExperiencia = horasExperiencia

    def obtenerHabilidades(self):
        return self.titulo