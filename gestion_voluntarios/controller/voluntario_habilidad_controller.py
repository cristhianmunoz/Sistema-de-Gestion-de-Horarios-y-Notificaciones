from django.shortcuts import redirect

from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.controller.voluntario_home_controller import comprobar_operacion_creacion
from gestion_voluntarios.controller.voluntario_home_controller import comprobar_operacion_eliminacion
from gestion_voluntarios.controller.voluntario_home_controller import comprobar_operacion_edicion


def index(request):
    id_voluntario = ''

    # Crear una habilidad
    if comprobar_operacion_creacion(request):
        # Obteniendo los parámetros enviados por POST
        id_voluntario = request.POST.get('id_voluntario')
        titulo_habilidad = request.POST.get('titulo_habilidad')
        descripcion_habilidad = request.POST.get('descripcion_habilidad')
        horas_experiencia_habilidad = request.POST.get('horas_experiencia_habilidad')

        # Comunicándose con los modelos para agregar una habilidad
        habilidad = Habilidad(
            titulo=titulo_habilidad,
            descripcion=descripcion_habilidad,
            horas_experiencia=int(horas_experiencia_habilidad),
            voluntario_id=id_voluntario
        )

        Habilidad.agregar_habilidad(habilidad)

    # Eliminar una habilidad
    elif comprobar_operacion_eliminacion(request):
        # Obteniendo los parámetros enviados por GET
        id_voluntario = request.POST.get('id_voluntario')
        id_habilidad = request.POST.get('id_habilidad')

        # Comunicándose con los modelos para eliminar la habilidad
        Habilidad.eliminar_habilidad(id_habilidad)

    # Editar una habilidad
    elif comprobar_operacion_edicion(request):
        id_voluntario = request.POST.get('id_voluntario')
        id_habilidad = request.POST.get('id_habilidad')
        titulo_habilidad = request.POST.get('titulo_habilidad')
        descripcion_habilidad = request.POST.get('descripcion_habilidad')
        horas_experiencia_habilidad = request.POST.get('horas_experiencia_habilidad')

        # Comunicándose con los modelos para editar una habilidad
        habilidad = Habilidad(
            id=id_habilidad,
            titulo=titulo_habilidad,
            descripcion=descripcion_habilidad,
            horas_experiencia=int(horas_experiencia_habilidad),
            voluntario_id=id_voluntario
        )

        Habilidad.editar_habilidad(habilidad)

    # Redirigiendo a voluntario home
    return redirect('/gestion_voluntarios/?id_voluntario=' + id_voluntario)
