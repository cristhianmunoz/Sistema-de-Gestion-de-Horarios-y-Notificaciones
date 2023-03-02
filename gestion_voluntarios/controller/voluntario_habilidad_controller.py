from django.shortcuts import render

from gestion_voluntarios.model.habilidad_model import Habilidad
from voluntario_home_controller import comprobar_operacion_creacion
from voluntario_home_controller import comprobar_operacion_eliminacion
from voluntario_home_controller import comprobar_operacion_edicion
from voluntario_home_controller import obtener_contexto


def index(request):
    id_voluntario = ''

    # Al recibir por POST se entiende que se quiere crear una habilidad
    if request.method == 'POST' and comprobar_operacion_creacion(request):
        # Obteniendo los parámetros enviados por POST
        id_voluntario = request.POST.get('id_voluntario')
        titulo_habilidad = request.POST.get('titulo_habilidad')
        descripcion_habilidad = request.POST.get('descripcion_habilidad')
        horas_experiencia_habilidad = request.POST.get('horas_experiencia_habilidad')

        # Comunicándose con los modelos para agregar una habilidad
        habilidad = Habilidad(
            titulo=titulo_habilidad,
            descripcion=descripcion_habilidad,
            horasExperiencia=horas_experiencia_habilidad,
            voluntario_id=id_voluntario
        )

        Habilidad.agregar_habilidad()

    # Al recibir por GET se entiende que se quiere eliminar o editar una habilidad
    elif request.method == 'GET' and comprobar_operacion_eliminacion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.GET.get('id_voluntario')
        id_habilidad = request.GET.get('id_habilidad')

        # Comunicándose con los modelos para eliminar la habilidad
        Habilidad.eliminar_habilidad()

    # Al recibir por GET se entiende que se quiere eliminar o editar una habilidad
    elif request.method == 'GET' and comprobar_operacion_edicion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.GET.get('id_voluntario')
        id_habilidad = request.GET.get('id_habilidad')
        titulo_habilidad = request.POST.get('titulo_habilidad')
        descripcion_habilidad = request.POST.get('descripcion_habilidad')
        horas_experiencia_habilidad = request.POST.get('horas_experiencia_habilidad')

        # Comunicándose con los modelos para editar una habilidad
        habilidad = Habilidad(
            id=id_habilidad,
            titulo=titulo_habilidad,
            descripcion=descripcion_habilidad,
            horasExperiencia=horas_experiencia_habilidad,
            voluntario_id=id_voluntario
        )

        Habilidad.editar_habilidad()

    # Comunicándose con los modelos para obtener los datos
    contexto = obtener_contexto(id_voluntario)

    # Enviando los datos obtenidos a la vista
    return render(request=request, template_name='voluntario_home_view.html', context=contexto)
