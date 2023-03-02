from django.db import models


class Horario(models.Model):
    voluntario = models.ForeignKey(
        'Voluntario',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='horario'
    )
