from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.habilidad_model import Habilidad

emergencia = Emergencia()


def index(request):
    # Obteniendo los parámetros enviados por GET
    id_voluntario = request.GET.get('id_voluntario')

    # Comunicándose con los modelos para obtener los datos
    contexto = obtener_contexto(4)

    # Enviando los datos obtenidos a la vista
    return render(request, 'priorizar_voluntario.html', contexto)


def obtener_contexto(id_volutario):
    voluntario = Voluntario.objects.all()
    print(voluntario)
    emergencia = Emergencia.objects.filter(id=1)
    print(emergencia[0].habilidad_requerida)
    emergencia.lista = voluntario
    print(emergencia.lista)
    return {'voluntario': voluntario, 'emergencia': emergencia}


def priorizar_voluntarios(request):
    print("Dentro de Priorizar voluntarios")

    habilidad = request.POST.get('habilidad')
    print(habilidad)
    emergencia = Emergencia.objects.get(id=1)
    print(emergencia.lista)
    voluntarios = emergencia.priorizar_voluntarios()

    print("HABILIDAD DENTRO DE PRIORIZAR_VOLUNTARIO")
    print(emergencia.habilidad_requerida)
    return render(request, 'priorizar_voluntario.html', {'voluntario': voluntarios})
