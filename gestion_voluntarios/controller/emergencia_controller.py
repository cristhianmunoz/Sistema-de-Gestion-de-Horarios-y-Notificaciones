from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario


def obtener_nombres_voluntario(voluntarios_seleccionados):
    nombres_voluntarios_prueba = []
    for voluntario in voluntarios_seleccionados:
        nombres_voluntarios_prueba.append(voluntario.nombre)
    return nombres_voluntarios_prueba


def solicitar_servicios_voluntarios(voluntarios, habilidades_requeridas):
    voluntarios_seleccionados = []
    for voluntario in voluntarios:
        if verificar_habilidades_requeridas(voluntario, habilidades_requeridas):
            voluntarios_seleccionados.append(voluntario)
    return voluntarios_seleccionados


def verificar_habilidades_requeridas(voluntario, habilidades_requeridas):
    # Ampliar más la logica para ver que sucede con las habilidades
    # Obtener la lista de habilidades requeridas y comparar con las habilidades del voluntario
    habilidad_requerida_usuario = []
    # Estas listas son con fines de prueba con base a lo que llegue en el feature
    habilidades_voluntarios = [Habilidad("Saturacion"), Habilidad("RCP"), Habilidad("Respiracion")]
    habilidades_requeridas = [Habilidad("Saturacion"), Habilidad("RCP")]

    # Voluntario seleccionados de prueba
    carlos = Voluntario("Carlos", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
    juan = Voluntario("Juan", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
    andres = Voluntario("Andres", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
    # LINEA IMPORTANTE
    # habilidades_voluntarios = voluntario.habilidades

    # Caso cuando las habilidades son exactamente las mismas
    if habilidades_requeridas == habilidades_voluntarios:

        return "si"
    else:
        # Caso cuando las habilidades de los voluntarios son mayores
        # Se compara la lista de habilidades requeridas con base en la lista de habilidades voluntario
        for habilidad_requerida in habilidades_requeridas:
            for habilidad_voluntario in habilidades_voluntarios:
                if habilidad_requerida.descripcion_habilidad == habilidad_voluntario.descripcion_habilidad:
                    habilidad_requerida_usuario.append(habilidad_requerida)
                    return "si"
                else:
                    return "no"


def enviar_notificaciones(voluntarios_seleccionados):
    aux = 0
    for voluntario in voluntarios_seleccionados:
        aux += 1
    return aux
