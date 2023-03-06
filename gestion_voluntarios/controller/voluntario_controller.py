from gestion_voluntarios.model.voluntario_model import Voluntario

voluntarios_de_prueba = [
    Voluntario("Carlos", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Juan", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Andres", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Kevin", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
]

"""def obtener_voluntarios_controller():
    # Se supone que existen ya voluntarios dentro de la base de datos
    # estos son simplemente voluntarios de prueba
    nombres_voluntarios_prueba = []
    for voluntario in voluntarios_de_prueba:
        nombres_voluntarios_prueba.append(voluntario.nombre)
    return nombres_voluntarios_prueba"""


def obtener_voluntarios_controller():
    # Obtiene los voluntarios registrados dentro de la base de datos
    return voluntarios_de_prueba
