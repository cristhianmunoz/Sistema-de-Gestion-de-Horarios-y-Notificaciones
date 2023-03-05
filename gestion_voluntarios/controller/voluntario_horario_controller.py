from datetime import time

from django.shortcuts import render, redirect

from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.controller.voluntario_home_controller import comprobar_operacion_creacion
from gestion_voluntarios.controller.voluntario_home_controller import comprobar_operacion_eliminacion
from gestion_voluntarios.controller.voluntario_home_controller import comprobar_operacion_edicion


def index(request):
    id_voluntario = ''

    # Crear un periodo
    if comprobar_operacion_creacion(request):
        # Obteniendo los parámetros enviados por POST
        id_voluntario = request.POST.get('id_voluntario')
        id_horario = request.POST.get('id_horario')
        dia_semana_periodo = request.POST.get('dia_semana_periodo')
        hora_inicio_periodo = request.POST.get('hora_inicio_periodo')
        hora_fin_periodo = request.POST.get('hora_fin_periodo')

        # Comunicándose con los modelos para agregar un periodo en el horario
        periodo = Periodo(
            diaSemana=dia_semana_periodo,
            horaInicio=hora_inicio_periodo,
            horaFin=hora_fin_periodo,
            horario_id=id_horario
        )

        Periodo.agregar_periodo(periodo)

    # Eliminar un periodo del horario
    elif comprobar_operacion_eliminacion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.POST.get('id_voluntario')
        id_periodo = request.POST.get('id_periodo')

        # Comunicándose con los modelos para eliminar el periodo del horario
        Periodo.eliminar_periodo(id_periodo)

    # Editar un periodo
    elif comprobar_operacion_edicion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.POST.get('id_voluntario')
        id_horario = request.POST.get('id_horario')
        id_periodo = request.POST.get('id_periodo')
        dia_semana_periodo = request.POST.get('dia_semana_periodo')
        hora_inicio_periodo = request.POST.get('hora_inicio_periodo')
        hora_fin_periodo = request.POST.get('hora_fin_periodo')

        parts_hora_inicio = hora_inicio_periodo.split(':')
        parts_hora_fin = hora_fin_periodo.split(':')

        # Comunicándose con los modelos para editar un periodo del horario
        periodo = Periodo(
            id=id_periodo,
            diaSemana=dia_semana_periodo,
            horaInicio=time(hour=int(parts_hora_inicio[0]), minute=int(parts_hora_inicio[1])),
            horaFin=time(hour=int(parts_hora_fin[0]), minute=int(parts_hora_fin[1])),
            horario_id=id_horario
        )

        Periodo.editar_periodo(periodo)

    # Redirigiendo a voluntario home
    return redirect('/gestion_voluntarios/?id_voluntario=' + id_voluntario)
