from gestion_voluntarios.model.voluntario_model import Voluntario

voluntarios_de_prueba = [
    Voluntario("Carlos", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Juan", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Andres", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Kevin", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')
]

vol = Voluntario("Carlos", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D')

voluntarios_de_prueba2 = [
    Voluntario("Carlos", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Juan", "Ramirez", 30, ['Saturacion', 'RCP', 'Respiracion'], 'D'),
    Voluntario("Andres", "Ramirez", 30, ['RCP'], 'D'),
    Voluntario("Kevin", "Ramirez", 30, ['Saturacion', 'RCP'], 'D')
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


def nombre_voluntario(voluntario):
    return vol.nombre


def obtener_voluntario():
    return vol

def obtener_voluntarios_controller2():
    # Obtiene los voluntarios registrados dentro de la base de datos
    return voluntarios_de_prueba2