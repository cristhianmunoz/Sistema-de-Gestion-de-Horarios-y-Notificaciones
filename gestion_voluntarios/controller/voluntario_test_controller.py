import datetime

from django.shortcuts import render

from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.dia_semana_model import DiaSemana


def index(request):
    voluntario_id = request.GET.get('id_voluntario')
    contexto = {}

    if voluntario_id:
        try:
            voluntario = Voluntario.objects.get(id=voluntario_id)
            habilidades = [
                Habilidad(titulo=HabilidadMedica.SUTURAR, descripcion='Suturar heridas', voluntario=voluntario),
            ]
            horario = Horario(voluntario=voluntario)
            periodos = [
                Periodo(diaSemana=DiaSemana.LUNES, horaInicio=datetime.time(7, 0, 0),
                        horaFin=datetime.time(9, 30, 0), horario=horario),
            ]
            contexto = {
                'voluntario': voluntario,
                'habilidades': habilidades,
                'horario': periodos,
                'catalogoHabilidades': HabilidadMedica.labels,
                'diasSemana': DiaSemana.labels,
                'horasPeriodo': obtenerHorasPeriodo()
            }
        except Voluntario.DoesNotExist:
            contexto = {}

    return render(request=request, template_name='voluntario_test_view.html', context=contexto)


def obtenerHorasPeriodo():
    hours = []
    for i in range(7, 17):
        hours.append(str(i) + ':00')
    return hours