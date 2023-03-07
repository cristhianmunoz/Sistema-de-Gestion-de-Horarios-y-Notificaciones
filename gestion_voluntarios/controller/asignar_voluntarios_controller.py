from django.http import HttpResponseRedirect
from django.shortcuts import render
from gestion_voluntarios.model.actividad_model import Actividad
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.emergencia_model import Emergencia


def index(request):
    print("Dentro del index")
    context = {}
    context.update(get_emergencia(request))
    return render(request, 'asignar_voluntarios.html', context)


def get_emergencia(request):
    emergencias = Emergencia.objects.all()
    for emergencia in emergencias:
        emergencia.nombre = emergencia.nombre.replace('"', '')
    context = {
        'emergencias': emergencias
    }
    return context


def asignar_voluntarios(request):
    print("Dentro de asignar_voluntarios")
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
                print("Emergencia " + str(emergencia_id) + " es Atendida: " + str(emergencia.get_es_atendida()))
        return HttpResponseRedirect('/gestion_voluntarios/actividad')
