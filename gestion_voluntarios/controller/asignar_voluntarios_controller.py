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
    for v in voluntarios:
        print(v.nombre)
    context = {
        'voluntarios': voluntarios
    }
    return context
