from django.http import HttpResponseRedirect

from gestion_voluntarios.models import Actividad, Voluntario


def cargar_actividades(request):
    actividades = Actividad.objects.all()
    for actividad in actividades:
        actividad.nombre = actividad.nombre.replace('"', '')
    context = {
        'actividades': actividades
    }
    return context


def get_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    context = {
        'voluntarios': voluntarios
    }
    return context


def asignar_voluntarios(request):
    if request.method == 'POST':
        if 'cerrar' in request.POST:
            print('boton cerrar')
        if 'guardar' in request.POST:
            print('boton guardar')
            voluntarios_seleccionados = request.POST.getlist("voluntarios")
            actividad_id = request.POST.get("actividad_id")
            print("actividad: " + actividad_id)
            print(voluntarios_seleccionados)
            actividad = Actividad.objects.get(pk=actividad_id)
            for voluntario_id in voluntarios_seleccionados:
                voluntario = Voluntario.objects.get(pk=voluntario_id)
                actividad.asignar_voluntario(voluntario)

                print("voluntario asignado a actividad")
        return HttpResponseRedirect('/gestion_voluntarios/')

