import django
from django.db import models

django.setup()


class Horario(models.Model):
    voluntario = models.ForeignKey(
        'Voluntario',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='horario'
    )

    @staticmethod
    def obtener_horario_por_id_voluntario(id_voluntario):
        try:
            horario = Horario.objects.get(voluntario_id=id_voluntario)
            return horario

        except Horario.DoesNotExist:
            return None
