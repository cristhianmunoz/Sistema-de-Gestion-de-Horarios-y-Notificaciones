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
        nombre='Francisco',
        apellido='Encalada',
        edad=23
    )
    context.voluntario.save()

    # Horario del voluntario
    context.horario = Horario(
        voluntario_id=context.voluntario.id
    )
    context.horario.save()

    # Periodo disponible
    context.periodo = Periodo(
<<<<<<< HEAD
        dia_semana=dia_disponible,
        hora_inicio=inicio_disponible,
        hora_fin=final_disponible,
=======
        diaSemana=dia_disponible,
        horaInicio=inicio_disponible,
        horaFin=final_disponible,
>>>>>>> e9e3ec81093607467fbd1cf2e5533b3ef58b840c
        horario_id=context.horario.id
    )
    context.periodo.save()


@step(
    'se requiera saber si el voluntario está disponible los días “{dia_solicitado}” en el periodo de '
    '“{inicio_solicitado}“ a “{final_solicitado}”'
)
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado):
    context.horario_solicitud = Horario()
    context.horario_solicitud.save()

    # Periodo solicitado
    context.periodo_solicitud = Periodo(
<<<<<<< HEAD
        dia_semana=dia_solicitado,
        hora_inicio=inicio_solicitado,
        hora_fin=final_solicitado,
=======
        diaSemana=dia_solicitado,
        horaInicio=inicio_solicitado,
        horaFin=final_solicitado,
>>>>>>> e9e3ec81093607467fbd1cf2e5533b3ef58b840c
        horario_id=context.horario_solicitud.id
    )
    context.periodo_solicitud.save()


@step('se tendrá que la disponibilidad del voluntario en el momento requerido es “{disponibilidad}”')
def step_impl(context, disponibilidad):
    disponibilidad_calculada = context.voluntario.comprobar_disponibilidad(context.periodo_solicitud)
    disponibilidad_recibida = disponibilidad == "True"

    assert disponibilidad_calculada == disponibilidad_recibida


@step('que el voluntario tiene registrados “{dias_disponibles_iniciales}” días disponibles')
def step_impl(context, dias_disponibles_iniciales):
    context.voluntario = Voluntario(
        nombre='Rafael',
        apellido='Pozo',
        edad=23
    )
    context.voluntario.save()

    context.horario = Horario(
        voluntario_id=context.voluntario.id
    )
    context.horario.save()


@step(
    'el voluntario quiera registrar su disponibilidad los días “{dia_solicitado}” en el periodo de '
    '“{inicio_solicitado}” a “{final_solicitado}” horas'
)
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado):
    id_horario = Horario.obtener_horario_por_id_voluntario(context.voluntario.id)
    context.nuevo_periodo = Periodo(
<<<<<<< HEAD
        dia_semana=dia_solicitado,
        hora_inicio=inicio_solicitado,
        hora_fin=final_solicitado,
=======
        diaSemana=dia_solicitado,
        horaInicio=inicio_solicitado,
        horaFin=final_solicitado,
>>>>>>> e9e3ec81093607467fbd1cf2e5533b3ef58b840c
        horario_id=id_horario
    )


@step('el voluntario tendrá registrados “{dias_disponibles_finales:f}” días disponibles')
def step_impl(context, dias_disponibles_finales):
    id_horario = Horario.obtener_horario_por_id_voluntario(context.voluntario.id)
    dias_disponibles_calculados = Periodo.obtener_cantidad_dias_disponibles(id_horario=id_horario)
    assert dias_disponibles_calculados == dias_disponibles_finales


@step('el voluntario estará disponible los días “{dia_disponible}” en el periodo de “{inicio_disponible}” a '
      '“{final_disponible}” horas')
def step_impl(context, dia_disponible, inicio_disponible, final_disponible):
    periodo_inicial = context.periodo
<<<<<<< HEAD
    assert periodo_inicial.dia_semana == dia_disponible
    assert periodo_inicial.hora_inicio == inicio_disponible
    assert periodo_inicial.hora_fin == final_disponible
=======
    assert periodo_inicial.diaSemana == dia_disponible
    assert periodo_inicial.horaInicio == inicio_disponible
    assert periodo_inicial.horaFin == final_disponible
>>>>>>> e9e3ec81093607467fbd1cf2e5533b3ef58b840c
