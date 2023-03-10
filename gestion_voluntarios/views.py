from django.http import HttpResponse
from django.shortcuts import render

from gestion_voluntarios.model.actividad_model import Actividad


def index(request):
    return HttpResponse("Hello from Django!")


def asignar_periodo(request, actividad_id):
    actividad = Actividad.objects.get(pk=actividad_id)
    horarios = actividad.horario_set.all()
    context = {
        'actividad': actividad,
        'horarios': horarios
    }
    return render(request, 'asignar_periodo.html', context)
