import random


def obtener_voluntarios_confirmados(lista_voluntarios, num_voluntarios_requeridos):
    lista_confirmados = []
    for i in range(num_voluntarios_requeridos):
        lista_confirmados.append(lista_voluntarios[i])

    return lista_confirmados


def contar_elementos(lista):
    contador = 0
    for x in lista:
        contador += 1

    return contador


def notificar(emergencia, lista_voluntarios):
    for voluntario in lista_voluntarios:
        texto = F'{emergencia.nombre} \n{emergencia.asunto} \nEstimado {voluntario.nombre}, se solicita su presencia en ' \
                F'{emergencia.ubicacion} a las {emergencia.hora_entrada}\n'
        print(texto)


def letra_random():
    letras = ['D', 'O']
    return random.choice(letras)


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
