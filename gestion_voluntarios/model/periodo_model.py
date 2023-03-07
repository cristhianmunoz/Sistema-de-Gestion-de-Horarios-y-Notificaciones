import datetime

import django
from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime as dt

from gestion_voluntarios.model.dia_semana_model import DiaSemana
from gestion_voluntarios.model.horario_model import Horario

django.setup()


class Periodo(models.Model):
    dia_semana = models.CharField(max_length=20, choices=DiaSemana.choices)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    horario = models.ForeignKey(
        'Horario',
        on_delete=models.CASCADE,
        related_name='periodos',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        # Comprobando que la hora de inicio no sea mayor a la hora de fin
        if not self.es_consistente():
            return

        # Comprobando que el periodo no choque con otro periodo existente
        if not self.no_tiene_conflicto():
            return

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
            Periodo.objects.filter(id=periodo.id).update(
                dia_semana=periodo.dia_semana,
                hora_inicio=periodo.hora_inicio,
                hora_fin=periodo.hora_fin
            )
            return True

        except ValidationError:
            return False

        except Periodo.DoesNotExist:
            return False

    @staticmethod
    def obtener_periodos_por_id_horario(id_horario):
        try:
            periodos = Periodo.objects.filter(horario_id=id_horario)
            return list(periodos)

        except Periodo.DoesNotExist:
            return None

    @staticmethod
    def obtener_periodo_por_id(id_periodo):
        try:
            periodo = Periodo.objects.get(id=id_periodo)
            return periodo

        except Periodo.DoesNotExist:
            return None

    @staticmethod
    def obtener_cantidad_dias_disponibles(id_horario):
        periodos = Periodo.obtener_periodos_por_id_horario(id_horario)
        set_dias = set()

        for periodo in periodos:
            set_dias.add(periodo.dia_semana)

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

    def es_consistente(self):
        if self.hora_inicio > self.hora_fin:
            return False
        return True

    def no_tiene_conflicto(self):
        periodos = Periodo.obtener_periodos_por_id_horario(self.horario.id)
        for periodo in periodos:
            # Comprobar: Si el día de la semana no coincide, continuar
            if periodo.dia_semana != self.dia_semana:
                continue
            # Comprobar: Si la hora de inicio está dentro de un periodo existente, continuar
            if not periodo.hora_inicio < self.hora_inicio < periodo.hora_fin:
                continue
            # Comprobar: Si la hora de fin está dentro de un periodo existente, continuar
            if not periodo.hora_inicio < self.hora_fin < periodo.hora_fin:
                continue
            return False

        return True

    @staticmethod
    def str_to_time(string):
        try:
            return dt.strptime(string, '%H:%M').time(), True
        except ValueError:
            return None, False
