from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from django.shortcuts import render
from gestion_voluntarios.controller.emergencia_controller import  solicitar_servicios_voluntarios

def index(request):
    print("Dentro del index")
    context = {}
    #context.update(get_emergencia(request))
    return render(request, 'notificacion.html', context)

def obtener_voluntarios_confirmados(lista_voluntarios):
    lista_confirmados = []
    for voluntario in lista_voluntarios:
        if voluntario.estado == 'D':
            lista_confirmados.append(voluntario)
    return lista_confirmados


def obtener_voluntarios_rechazados(lista_voluntarios):
    lista_rechazos = []
    for voluntario in lista_voluntarios:
        if voluntario.estado == 'O':
            lista_rechazos.append(voluntario)

    return lista_rechazos


def contar_elementos(lista):
    contador = 0
    for x in lista:
        contador += 1

    return contador


def obtener_nombres(lista):
    aux_lista = ""
    if len(lista) == 0:
        aux_lista = "null"
        return aux_lista
    tamanio = len(lista)
    for voluntario in lista:
        if lista.index(voluntario) < tamanio - 1:
            aux_lista += voluntario.to_string() + ", "
        else:
            aux_lista += voluntario.to_string()
    return aux_lista

def ver_notificacion(request):
    print("id_voluntario",request.POST.get('id_voluntario'))
    context = {}
    if request.method == "POST":
        if "ver_notificaciones" == request.POST.get('operacion'):
            id_voluntario = request.POST.get('id_voluntario')
            voluntario = Voluntario.obtener_voluntario_por_id(id_voluntario)
            emergencia = Emergencia.obtener_emergencia_por_id(voluntario.emergencia_id)
            if emergencia.activada == True:
                emergencia_activada = emergencia
                voluntarios_seleccionados = solicitar_servicios_voluntarios(Voluntario.get_voluntarios(), emergencia)
                context = {'emergencia': emergencia_activada, 'voluntarios':voluntarios_seleccionados}
    return render(request,'notificacion.html', context)


