import django
from django.db import models
from django.db import connection

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo

django.setup()


class Actividad(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default='')
    tiene_voluntario = models.BooleanField(default=False)
    emergencia = models.ForeignKey(Emergencia,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True,
                                   related_name='actividades'
                                   )
    # Revisar esta relación (una actividad muchos voluntarios - un voluntario muchas actividades)
    voluntarios = models.ManyToManyField('Voluntario')

    def asignar_voluntario(self, voluntario):
        self.voluntarios.add(voluntario)
        self.tiene_voluntario = True
        voluntario.es_asignado = True
        voluntario.save()
        self.save()

    def get_tiene_voluntario(self):
        return self.tiene_voluntario

    def get_voluntarios(self):
        return self.voluntarios.all()

    def get_periodos(self):
        horario = Horario.obtener_horario_por_id_actividad(self.id)
        periodos = Periodo.obtener_periodos_por_id_horario(horario.id)

        return periodos

    def obtenerActividadesCriticas(self, lista_actividades, lista_voluntarios):
        actividades_sin_match = []
        flag = False

        for voluntario in lista_voluntarios:
            for actividad in lista_actividades:
                periodos = actividad.get_periodos()
                for indice, periodo in enumerate(periodos):
                    if not voluntario.comprobar_disponibilidad(periodo):
                        actividades_sin_match.append(actividad)

        return actividades_sin_match

    def get_actividad_str(self):
        nombre=self.nombre
        emergencia=self.emergencia.nombre
        strPeriodos=''
        periodos = self.get_periodos()
        for periodo in periodos:
            strPeriodos = strPeriodos + '\n' + periodo.dia_semana + " - " + periodo.hora_inicio + " -> " + periodo.hora_fin

        obj = {
            "periodos": strPeriodos,
            "nombre": nombre,
            "emergencia": emergencia
        }
        return obj