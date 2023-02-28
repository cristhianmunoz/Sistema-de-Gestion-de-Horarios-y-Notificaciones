from behave import *

use_step_matcher("parse")


@step(
    'que el voluntario está disponible los días “{dia_disponible}” en el periodo de “{inicio_disponible}” a '
    '“{final_disponible}” horas'
)
def step_impl(context, dia_disponible, inicio_disponible, final_disponible):
    pass


@step(
    'se requiera saber si el voluntario está disponible los días “{dia_solicitado}” en el periodo de '
    '“{inicio_solicitado}“ a “{final_solicitado}”'
)
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado):
    pass


@step('se tendrá que la disponibilidad del voluntario en el momento requerido es “{disponibilidad}”')
def step_impl(context, disponibilidad):
    pass


@step('que el voluntario tiene registrados “{dias_disponibles_iniciales}” días disponibles')
def step_impl(context, dias_disponibles_iniciales):
    pass


@step(
    'el voluntario quiera registrar su disponibilidad los días “{dia_solicitado}” en el periodo de '
    '“{inicio_solicitado}” a “{final_solicitado}” horas'
)
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado):
    pass


@step('el voluntario tendrá registrados “{dias_disponibles_finales}” días disponibles')
def step_impl(context, dias_disponibles_finales):
    pass


@step('el voluntario estará disponible los días “{dia_disponible}” en el periodo de “{inicio_disponible}” a '
      '“{final_disponible}” horas')
def step_impl(context, dia_disponible, inicio_disponible, final_disponible):
    pass
