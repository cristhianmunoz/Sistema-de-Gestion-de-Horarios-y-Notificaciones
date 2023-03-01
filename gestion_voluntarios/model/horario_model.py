from django.db import models

from gestion_voluntarios.model.periodo_model import Periodo


class Horario(models.Model):
    periodos = models.ManyToManyField(Periodo)
    voluntario = models.ForeignKey('Voluntario', on_delete=models.CASCADE)
