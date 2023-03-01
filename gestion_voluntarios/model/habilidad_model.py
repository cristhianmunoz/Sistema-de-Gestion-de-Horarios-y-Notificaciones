from django.db import models

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.voluntario_model import Voluntario


class Habilidad(models.Model):
    titulo = models.CharField(max_length=20, choices=HabilidadMedica.choices)
    descripcion = models.CharField(max_length=200, default='')
    horasExperiencia = models.PositiveIntegerField(default=0)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
