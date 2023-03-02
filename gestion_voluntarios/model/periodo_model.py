from django.core.exceptions import ValidationError
from django.db import models

from gestion_voluntarios.model.dia_semana_model import DiaSemana


class Periodo(models.Model):
    diaSemana = models.CharField(max_length=20, choices=DiaSemana.choices)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    horario = models.ForeignKey('Horario', on_delete=models.CASCADE, related_name='periodos')

    def agregar_periodo(self):
        try:
            periodo_nuevo = Periodo(
                diaSemana=self.diaSemana,
                horaInicio=self.horaInicio,
                horaFin=self.horaFin,
                horario=self.horario
            )
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
