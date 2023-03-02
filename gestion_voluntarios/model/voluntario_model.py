from django.db import models
from django.utils.dateparse import parse_time


class Voluntario(models.Model):
    # Campos de la clase Voluntario
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)

    def comprobar_disponibilidad(self, horario):
        # Itera por cada periodo del horario
        for periodo_horario in horario.periodos.all():
            # Itera por cada periodo del horario del voluntario
            for periodo_voluntario in self.horario.periodos.all():
                # Períodos del horario
                inicio_horario = parse_time(periodo_horario.inicio)
                fin_horario = parse_time(periodo_horario.fin)
                # Periodos del horario del voluntario
                inicio_horario_voluntario = parse_time(periodo_voluntario.inicio)
                fin_horario_voluntario = parse_time(periodo_voluntario.fin)
                # Revisa si los periodos se chocan entre sí
                if max(inicio_horario, inicio_horario_voluntario) <= min(fin_horario, fin_horario_voluntario):
                    # Los periodos chocan entre sí - Voluntario no disponible
                    return False
        # Los horarios no se chocan entre sí - Voluntario disponible
        return True

    # Toma al Voluntario de acuerdo a su ID
    @classmethod
    def obtener_voluntario_por_id(cls, id_voluntario):
        try:
            # Intenta obtener el voluntario que coincide con ese ID
            voluntario = Voluntario.objects.get(id=id_voluntario)
            return voluntario
        except Voluntario.DoesNotExist:
            # Retornar None en caso de que no se haya encontrado el Voluntario
            return None

