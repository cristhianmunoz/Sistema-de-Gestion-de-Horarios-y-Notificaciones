from django.shortcuts import render

from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario


def index(request):
    # Obteniendo los parámetros enviados por GET
    id_voluntario = request.GET.get('id_voluntario')

    # Comunicándose con los modelos para obtener los datos
    contexto = obtener_contexto(id_voluntario)

    # Enviando los datos obtenidos a la vista
    return render(request=request, template_name='voluntario_home_view.html', context=contexto)


def comprobar_operacion_creacion(request):
    operacion = request.POST.get('operacion')
    return operacion and operacion == 'creacion'


def comprobar_operacion_eliminacion(request):
    operacion = request.GET.get('operacion')
    return operacion and operacion == 'eliminacion'


def comprobar_operacion_edicion(request):
    operacion = request.GET.get('operacion')
    return operacion and operacion == 'edicion'


def obtener_contexto(id_voluntario):
    voluntario = Voluntario.obtener_voluntario_por_id()
    habilidades = Habilidad.obtener_habilidades_por_id_voluntario(id_voluntario)
    horario = Horario.obtener_horario_por_id_voluntario(id_voluntario)
    periodos = Periodo.obtener_periodos_por_id_voluntario(id_voluntario)
    horario.periodos = periodos

    return {
        'voluntario': voluntario,
        'habilidades': habilidades,
        'horario': horario
    }
