from django.shortcuts import render

from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario


def index(request):
    # Obteniendo los parámetros enviados por GET
    id_voluntario = request.GET.get('id_voluntario')

    # Comunicándose con los modelos para obtener los datos
    contexto = obtenerContexto(id_voluntario)

    # Enviando los datos obtenidos a la vista
    return render(request=request, template_name='voluntario_home_view.html', context=contexto)


def comprobarOperacionCreacion(request):
    operacion = request.POST.get('operacion')
    return operacion and operacion == 'creacion'


def comprobarOperacionEliminacion(request):
    operacion = request.GET.get('operacion')
    return operacion and operacion == 'eliminacion'


def comprobarOperacionEdicion(request):
    operacion = request.GET.get('operacion')
    return operacion and operacion == 'edicion'


def obtenerContexto(id_voluntario):
    voluntario = Voluntario.obtenerVoluntarioPorID(id_voluntario)
    habilidades = Habilidad.obtenerHabilidadesPorIDVoluntario(id_voluntario)
    horario = Horario.obtenerHorarioPorIDVoluntario(id_voluntario)
    periodos = Periodo.obtenerPeriodosPorIDVoluntario(id_voluntario)
    horario.periodos = periodos

    return {
        'voluntario': voluntario,
        'habilidades': habilidades,
        'horario': horario
    }
