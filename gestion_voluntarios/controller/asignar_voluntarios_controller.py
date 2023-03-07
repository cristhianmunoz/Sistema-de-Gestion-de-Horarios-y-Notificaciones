from django.http import HttpResponseRedirect

from gestion_voluntarios.models import Actividad, Voluntario, Emergencia


def get_emergencia(request):
    emergencias = Emergencia.objects.all()
    for emergencia in emergencias:
        emergencia.nombre = emergencia.nombre.replace('"', '')
    context = {
        'emergencias': emergencias
    }
    return context


def get_emergencia_voluntario(request):
    emergencias = Emergencia.objects.all()
    context = {
        'emergencias': emergencias
    }
    return context


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


def get_id_emergencia(request):
    print("entra a get id")
    if request.method == 'POST':
        emergencia_id = request.POST.get("emergencia_id")
        print("emergencia: " + emergencia_id)
        emergencia = Emergencia.objects.get(pk=emergencia_id)


def asignar_voluntarios(request):
    if request.method == 'POST':
        if 'cerrar' in request.POST:
            # Emergencia
            emergencia_id = request.POST.get("emergencia_id")
            print("Emergencia: " + emergencia_id)
            # Actividad
            actividad_id = request.POST.get("actividad_id")
            print("Actividad: " + actividad_id)
            print('boton cerrar')
        if 'guardar' in request.POST:
            print('boton guardar')
            # Emergencia
            emergencia_id = request.POST.get("emergencia_id")
            print("Emergencia: " + emergencia_id)
            # Actividad
            actividad_id = request.POST.get("actividad_id")
            print("actividad: " + actividad_id)
            # Voluntarios
            voluntarios_seleccionados = request.POST.getlist("ids_voluntarios")
            print(voluntarios_seleccionados)

            actividad = Actividad.objects.get(pk=actividad_id)
            emergencia = Emergencia.objects.get(pk=emergencia_id)

            for voluntario_id in voluntarios_seleccionados:

                voluntario = Voluntario.objects.get(pk=voluntario_id)
                actividad.asignar_voluntario(voluntario)
                emergencia.verificar_emergencia()

                print("voluntario asignado a actividad")
                print("Emergencia " + str(emergencia_id) + " es Atentida: "+str(emergencia.get_es_atendida()))
        return HttpResponseRedirect('/gestion_voluntarios/')
