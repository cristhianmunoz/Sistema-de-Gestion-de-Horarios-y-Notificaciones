from django.db import models


class HabilidadMedica(models.TextChoices):
    SUTURAR = 'Suturar'
    VACUNAR = 'Vacunar'
    ANESTESIAR = 'Anestesiar'
