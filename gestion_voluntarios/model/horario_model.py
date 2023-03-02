from django.db import models


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
        horario = Horario.objects.get(voluntario_id=id_voluntario)
        return horario
