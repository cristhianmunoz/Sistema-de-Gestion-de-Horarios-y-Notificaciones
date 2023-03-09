from django.shortcuts import render

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario


def index(request):
    # Comunicándose con los modelos para obtener los datos
    contexto = traer_voluntarios(request)
    # Enviando los datos obtenidos a la vista
    return render(request, 'priorizar_voluntario.html', contexto)


def traer_voluntarios(request):
    voluntarios_priorizada = []
    habilidad = []
    emergencias = list(Emergencia.objects.all())
    for emergencia in emergencias:
        emergencia.lista = list(Voluntario.objects.filter(emergencia_id=emergencia.id))
        habilidad.append(emergencia.priorizar_voluntarios())
        voluntarios_priorizada.append(emergencia.obtener_lista_voluntarios())
    return {'voluntarios': voluntarios_priorizada, 'emergencias': emergencias, 'habilidades': habilidad}
