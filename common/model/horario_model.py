from django.db import models

from common.model.periodo_model import Periodo


class Horario(models.Model):
    periodos = models.ManyToManyField(Periodo)
