def obtener_nombres_voluntario(voluntarios_seleccionados):
    nombres_voluntarios_prueba = []
    for voluntario in voluntarios_seleccionados:
        nombres_voluntarios_prueba.append(voluntario.nombre)
    return nombres_voluntarios_prueba


def solicitar_servicios_voluntarios(voluntarios, habilidades_requeridas):
    voluntarios_seleccionados = []
    for voluntario in voluntarios:
        if verificar_habilidades_requeridas(voluntario.habilidades, habilidades_requeridas):
            voluntarios_seleccionados.append(voluntario)
    return voluntarios_seleccionados


def verificar_habilidades_requeridas(habilidades_voluntarios, habilidades_requeridas):
    # Ampliar mas la logica para ver que sucede con las habilidades
    if habilidades_requeridas == habilidades_voluntarios:
        return "si"
    else:
        return "no"


def enviar_notificaciones(voluntarios_seleccionados):
    aux = 0
    for voluntario in voluntarios_seleccionados:
        aux += 1
    return aux
