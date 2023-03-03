import django
from django.db import models

from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo

django.setup()


class Voluntario(models.Model):
    def __init__(self, nombre, apellido, edad, habilidades, estado, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.habilidades = habilidades
        self.estado = estado

    # Campos de la clase Voluntario
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)
    habilidades = models.CharField(max_length=500, default='')
    estado = models.CharField(max_length=1, default="D")

    def comprobar_disponibilidad(self, periodo_a_comprobar):
        periodos = Periodo.obtener_periodos_por_id_horario(Horario.obtener_horario_por_id_voluntario(self.id).id)
        periodo_a_comprobar_aux = Periodo.obtener_periodo_por_id(periodo_a_comprobar.id)


        for periodo in periodos:
            if periodo.diaSemana != periodo_a_comprobar.diaSemana:
                continue
            if periodo.horaInicio > periodo_a_comprobar.horaInicio:
                continue
            if periodo.horaInicio < periodo_a_comprobar.horaFin:

        # comprobar la disponibilidad por etapas
                for periodo in periodos:
                    if periodo.diaSemana != periodo_a_comprobar_aux.diaSemana:
                        continue
                    if periodo.horaInicio > periodo_a_comprobar_aux.horaInicio:
                        continue
                    if periodo.horaFin < periodo_a_comprobar_aux.horaFin:

                        continue
                    return True

        return False

    """def comprobar_disponibilidad(self, horario):
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
        return True"""

    # Toma al Voluntario de acuerdo a su ID
    @staticmethod
    def obtener_voluntario_por_id(id_voluntario):

        try:
            # Intenta obtener el voluntario que coincide con ese ID
            voluntario = Voluntario.objects.get(id=id_voluntario)
            return voluntario
        except Voluntario.DoesNotExist:
            # Retornar None en caso de que no se haya encontrado el Voluntario
            return None
