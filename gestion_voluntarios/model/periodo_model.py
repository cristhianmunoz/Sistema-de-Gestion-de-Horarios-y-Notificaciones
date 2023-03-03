import django
from django.core.exceptions import ValidationError
from django.db import models

from gestion_voluntarios.model.dia_semana_model import DiaSemana
from gestion_voluntarios.model.horario_model import Horario

django.setup()


class Periodo(models.Model):
    diaSemana = models.CharField(max_length=20, choices=DiaSemana.choices)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    horario = models.ForeignKey(
        'Horario',
        on_delete=models.CASCADE,
        related_name='periodos',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        # Validar que periodo tenga lógica
        if self.horaInicio > self.horaFin:
            return False

        # Validar que el periodo creado no se cruce con otro periodo existente
        periodos = Periodo.obtener_periodos_por_id_horario(self.horario.id)
        for periodo in periodos:
            if periodo.diaSemana != self.diaSemana:
                continue
            if periodo.horaInicio < self.horaInicio < periodo.horaFin:
                continue
            if periodo.horaInicio < self.horaFin < periodo.horaFin:
                continue

        super().save(*args, **kwargs)

    @staticmethod
    def agregar_periodo(periodo):
        try:
            periodo.save()
            return True

        except ValidationError:
            return False

    @staticmethod
    def eliminar_periodo(id_periodo):
        try:
            Periodo.objects.get(id=id_periodo).delete()
            return True

        except Periodo.DoesNotExist:
            return False

    @staticmethod
    def editar_periodo(periodo):
        try:
            periodo.save()
            return True

        except ValidationError:
            return False

    @staticmethod
    def obtener_periodos_por_id_horario(id_horario):
        periodos = Periodo.objects.filter(horario_id=id_horario)
        return list(periodos)

    @staticmethod
    def obtener_periodo_por_id(id_periodo):
        periodo = Periodo.objects.get(id=id_periodo)
        return periodo

    @staticmethod
    def obtener_cantidad_dias_disponibles(id_horario):
        periodos = Periodo.obtener_periodos_por_id_horario(id_horario)
        set_dias = set()
        for periodo in periodos:
            set_dias.add(periodo.diaSemana)

        return len(set_dias)

    @staticmethod
    def obtener_periodos_por_id_voluntario(id_voluntario):
        try:
            horario = Horario.obtener_horario_por_id_voluntario(id_voluntario)

            if horario is not None:
                periodos = Periodo.objects.filter(horario_id=horario.id)
                return periodos

        except Periodo.DoesNotExist:
            return None
