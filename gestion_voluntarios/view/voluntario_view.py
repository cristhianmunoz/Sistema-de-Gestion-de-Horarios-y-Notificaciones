from django.shortcuts import render
from gestion_voluntarios.controller import asignar_voluntarios_controller


def index(request):
    context = {}
    context.update(render_actividades(request))
    context.update(popup_voluntarios(request))
    return render(request, 'gestion_voluntarios/asignar_voluntarios.html', context)


def render_actividades(request):
    context = asignar_voluntarios_controller.cargar_actividades(request)
    return context


def popup_voluntarios(request):
    context = asignar_voluntarios_controller.get_voluntarios(request)
    return context

