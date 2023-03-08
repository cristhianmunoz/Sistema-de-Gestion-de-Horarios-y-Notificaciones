def obtener_voluntarios_confirmados(lista_voluntarios):
    lista_confirmados = []
    for voluntario in lista_voluntarios:
        if voluntario.estado == 'O':
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
