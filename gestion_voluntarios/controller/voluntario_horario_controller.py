from django.shortcuts import render

from gestion_voluntarios.model.periodo_model import Periodo
from voluntario_home_controller import comprobar_operacion_creacion
from voluntario_home_controller import comprobar_operacion_eliminacion
from voluntario_home_controller import comprobar_operacion_edicion
from voluntario_home_controller import obtener_contexto


def index(request):
    id_voluntario = ''

    # Al recibir por POST se entiende que se quiere crear un horario
    if request.method == 'POST' and comprobar_operacion_creacion(request):
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

    # Al recibir por GET se entiende que se quiere eliminar o editar un periodo del horario
    elif request.method == 'GET' and comprobar_operacion_eliminacion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.GET.get('id_voluntario')
        id_periodo = request.GET.get('id_periodo')

        # Comunicándose con los modelos para eliminar el periodo del horario
        Periodo.eliminar_periodo(id_periodo)

    # Al recibir por GET se entiende que se quiere eliminar o editar una habilidad
    elif request.method == 'GET' and comprobar_operacion_edicion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.GET.get('id_voluntario')
        id_horario = request.GET.get('id_horario')
        id_periodo = request.GET.get('id_periodo')
        dia_semana_periodo = request.GET.get('dia_semana_periodo')
        hora_inicio_periodo = request.GET.get('hora_inicio_periodo')
        hora_fin_periodo = request.GET.get('hora_fin_periodo')

        # Comunicándose con los modelos para editar un periodo del horario
        periodo = Periodo(
            id=id_periodo,
            diaSemana=dia_semana_periodo,
            horaInicio=hora_inicio_periodo,
            horaFin=hora_fin_periodo,
            horario_id=id_horario
        )

        Periodo.editar_periodo(periodo)

    # Comunicándose con los modelos para obtener los datos
    contexto = obtener_contexto(id_voluntario)

    # Enviando los datos obtenidos a la vista
    return render(request=request, template_name='voluntario_home_view.html', context=contexto)
