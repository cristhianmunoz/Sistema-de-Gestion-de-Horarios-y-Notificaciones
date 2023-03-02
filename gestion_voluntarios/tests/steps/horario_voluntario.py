from behave import *

from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")


@step(
    'que el voluntario está disponible los días “{dia_disponible}” en el periodo de “{inicio_disponible}” a '
    '“{final_disponible}” horas'
)
def step_impl(context, dia_disponible, inicio_disponible, final_disponible):
    # Voluntario
    context.voluntario = Voluntario(
        id=2,
        nombre='Francisco',
        apellido='Encalada',
        edad=23
    )
    context.voluntario.save()

    # Horario del voluntario
    context.horario = Horario(
        id=2,
    )
    context.horario.save()

    # Periodo disponible
    context.periodo = Periodo(
        id=1,
        diaSemana=dia_disponible,
        horaInicio=inicio_disponible,
        horaFin=final_disponible,
        horario_id=2
    )
    context.periodo.save()


@step(
    'se requiera saber si el voluntario está disponible los días “{dia_solicitado}” en el periodo de '
    '“{inicio_solicitado}“ a “{final_solicitado}”'
)
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado):
    # Periodo solicitado
    context.periodo_solicitud = Periodo(
        id=2,
        diaSemana=dia_solicitado,
        horaInicio=inicio_solicitado,
        horaFin=final_solicitado,
        horario_id=2
    )
    context.periodo_solicitud.save()


@step('se tendrá que la disponibilidad del voluntario en el momento requerido es “{disponibilidad}”')
def step_impl(context, disponibilidad):
    context.voluntario.comprobar_disponibilidad(context.periodo_solicitud)


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
