from django.db import models

from gestion_voluntarios.model.dia_semana_model import DiaSemana


class Periodo(models.Model):
    diaSemana = models.CharField(choices=DiaSemana.choices)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    horario = models.ForeignKey('Horario', on_delete=models.CASCADE)