from behave import *

use_step_matcher("parse")


@step(
    'que el voluntario tiene registrada “{cantidad_habilidades_registradas:f}” habilidad médica con el título '
    '“{titulo_habilidad}” con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, cantidad_habilidades_registradas, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    pass


@step(
    'únicamente existen las habilidades médicas “{habilidad_suturar}”, “{habilidad_vacunar}” y “{habilidad_anestesiar}”'
)
def step_impl(context, habilidad_suturar, habilidad_vacunar, habilidad_anestesiar):
    pass


@step(
    'el voluntario intente registrar una nueva habilidad médica con el título “{titulo_habilidad}”, '
    'con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    pass


@step(
    'el voluntario tendrá registrada “{cantidad_habilidades_registradas:f}” habilidad médica con el título '
    '“{titulo_habilidad}”, con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, cantidad_habilidades_registradas, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    pass


@step('que el voluntario tiene registradas “{cantidad_habilidades_registradas:f}” habilidades médicas')
def step_impl(context, cantidad_habilidades_registradas):
    pass


@step('el voluntario tendrá registradas “{cantidad_habilidades_registradas:f}” habilidades médicas')
def step_impl(context, cantidad_habilidades_registradas):
    pass


@step(
    'el voluntario tendrá registrada “{cantidad_habilidades_registradas:f}” habilidad médica registrada con el título '
    '“{titulo_habilidad}”, con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, cantidad_habilidades_registradas, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    pass
