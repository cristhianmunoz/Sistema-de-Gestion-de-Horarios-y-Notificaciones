habilidades_voluntario_scenarios = [
    'El voluntario intenta registrar una habilidad médica registrada previamente',
    'El voluntario intenta registrar una habilidad médica que no existe',
    'El voluntario registra una nueva habilidad médica',
    'El voluntario intenta registrar una habilidad médica con horas de experiencia incorrectas'
]

def after_scenario(context, scenario):
    if scenario.name in habilidades_voluntario_scenarios:
        pass
