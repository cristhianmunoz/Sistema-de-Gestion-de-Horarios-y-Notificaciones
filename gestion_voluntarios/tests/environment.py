from gestion_voluntarios.model.voluntario_model import Voluntario

# Listado de escenarios del feature habilidades_voluntario
habilidades_voluntario_scenarios = [
    'El voluntario intenta registrar una habilidad médica registrada previamente',
    'El voluntario intenta registrar una habilidad médica que no existe',
    'El voluntario registra una nueva habilidad médica',
    'El voluntario intenta registrar una habilidad médica con horas de experiencia incorrectas -- @1.1 ',
    'El voluntario intenta registrar una habilidad médica con horas de experiencia incorrectas -- @1.2 '
]

# Listado de escenarios del feature horario_voluntario
horario_voluntario_scenarios = [
    'Se comprueba la disponibilidad del voluntario en un horario específico -- @1.1 ',
    'Se comprueba la disponibilidad del voluntario en un horario específico -- @1.2 ',
    'Se comprueba la disponibilidad del voluntario en un horario específico -- @1.3 ',
    'Se comprueba la disponibilidad del voluntario en un horario específico -- @1.4 ',
    'El voluntario intenta registrar horarios de disponibilidad con horas incorrectas -- @1.1 ',
    'El voluntario intenta registrar horarios de disponibilidad con horas incorrectas -- @1.2 ',
    'El voluntario intenta registrar horarios de disponibilidad con horas incorrectas -- @1.3 ',
    'El voluntario registra su horario de disponibilidad'
]


def after_scenario(context, scenario):
    # Ejecutando pasos después de cada escenario del feature habilidades_voluntario
    if scenario.name in habilidades_voluntario_scenarios:
        after_habilidades_voluntario_scenarios(context)

    # Ejecutando pasos después de cada escenario del feature horario_voluntario
    if scenario.name in horario_voluntario_scenarios:
        after_horario_voluntario_scenarios(context)


def after_habilidades_voluntario_scenarios(context):
    Voluntario.obtener_voluntario_por_id(context.voluntario.id).delete() # +++++++++++++++++++++++++++++++++++++++++++++++++


def after_horario_voluntario_scenarios(context):
    Voluntario.obtener_voluntario_por_id(context.voluntario.id).delete()  # +++++++++++++++++++++++++++++++++++++++++++++++++
