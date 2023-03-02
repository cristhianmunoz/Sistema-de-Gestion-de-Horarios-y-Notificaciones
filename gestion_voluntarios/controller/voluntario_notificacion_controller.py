def obtener_voluntarios_confirmados(lista_voluntarios):
    lista_confirmados = []
    for voluntario in lista_voluntarios:
        #print(voluntario)
        if voluntario.estado == 'D':
            lista_confirmados.append(voluntario)
    #print(lista_confirmados)
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
