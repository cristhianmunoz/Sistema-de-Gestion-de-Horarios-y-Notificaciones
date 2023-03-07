from django.shortcuts import render
from gestion_voluntarios.controller import asignar_voluntarios_controller


def index(request):
    context = {}
    context.update(render_emergencia(request))
    return render(request, 'gestion_voluntarios/asignar_voluntarios.html', context)


def render_emergencia(request):
    context = asignar_voluntarios_controller.get_emergencia(request)
    return context


