from django.db import models

from common.model.dia_semana_model import DiaSemana


class Periodo(models.Model):
    diaSemana = models.CharField(choices=DiaSemana.choices)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
