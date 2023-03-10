from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from gestion_voluntarios.model.actividad_model import Actividad
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario


def index(request):
    context = {}
    context.update(devolver_emergencia(request))
    context.update(devolver_actividades(request))
    context.update(devolver_horarios(request))
    context.update(devolver_periodos(request))
    context.update(devolver_voluntarios(request))
    context.update(devolver_voluntarios_no_asignados())
    return render(request, 'gestion_horarios.html', context)


def asignar_periodo(request, horario_id):
    horario = get_object_or_404(Horario, pk=horario_id)
    if request.method == 'POST':
        dia_semana = request.POST['dia_semana']
        hora_inicio = request.POST['hora_inicio']
        hora_fin = request.POST['hora_fin']
        periodo = Periodo.objects.create(dia_semana=dia_semana, hora_inicio=hora_inicio, hora_fin=hora_fin)
        horario.periodos.add(periodo)
        return redirect('detalle_horario', horario_id=horario_id)
    return render(request, 'asignar_periodo.html', {'horario': horario})


def devolver_emergencia(request):
    emergencias = Emergencia.objects.all()
    for emergencia in emergencias:
        emergencia.nombre = emergencia.nombre.replace('"', '')
    context = {
        'emergencias': emergencias
    }
    return context


def devolver_actividades(request):
    actividades = list(Actividad.objects.all())
    context = {
        'actividades': actividades
    }
    return context


def devolver_horarios(request):
    horarios = list(Horario.objects.all())
    context = {
        'horarios': horarios
    }
    return context


def devolver_periodos(request):
    periodos = list(Periodo.objects.all())
    context = {
        'periodos': periodos
    }
    return context


def devolver_voluntarios(request):
    voluntarios = list(Voluntario.objects.all())
    context = {
        'voluntarios': voluntarios
    }
    return context


def devolver_voluntarios_no_asignados():
    voluntarios = list(Voluntario.objects.filter(es_asignado=0))
    context = {
        'voluntarios_no_asig': voluntarios
    }
    return context
