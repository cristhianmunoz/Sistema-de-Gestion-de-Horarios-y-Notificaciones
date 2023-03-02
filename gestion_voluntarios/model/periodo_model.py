import django
from django.core.exceptions import ValidationError
from django.db import models

from gestion_voluntarios.model.dia_semana_model import DiaSemana

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

    def agregar_periodo(self):
        try:
            periodo_nuevo = Periodo(
                diaSemana=self.diaSemana,
                horaInicio=self.horaInicio,
                horaFin=self.horaFin,
                horario=self.horario
            )
            # validar que periodo tenga lógica
            if self.horaInicio > self.horaFin:
                return False

            # validar que el periodo creado no se cruce con otro periodo existente
            periodos = Periodo.obtener_periodos_por_id_horario(self.horario.id)
            for periodo in periodos:
                if periodo.diaSemana != self.diaSemana:
                    continue
                if periodo.horaInicio < self.horaInicio < periodo.horaFin:
                    continue
                if periodo.horaInicio < self.horaFin < periodo.horaFin:
                    continue

            # validar los campos del modelo antes de guardarlo
            periodo_nuevo.full_clean()
            periodo_nuevo.save()
            return True
        except ValidationError:
            # Maneja la excepción de validación de campos requeridos
            return False

    @classmethod
    def eliminar_periodo(cls, id_periodo):
        try:
            periodo = Periodo.objects.get(id=id_periodo)
            periodo.delete()
            return True
        except Periodo.DoesNotExist:
            return False

    def editar_periodo(self):
        try:
            periodo_existente = self.objects.get(id=self.id)
            periodo_existente.diaSemana = self.diaSemana
            periodo_existente.horaInicio = self.horaInicio
            periodo_existente.horaFin = self.horaFin
            periodo_existente.save()
            return True
        except Periodo.DoesNotExist:
            # Maneja la excepción si el Periodo no existe para actualizarla
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

