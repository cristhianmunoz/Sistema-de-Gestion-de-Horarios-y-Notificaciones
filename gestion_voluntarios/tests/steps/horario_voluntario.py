import random

from behave import *
from faker import Faker

from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")
fake = Faker('es_ES')


@step(
    'que el voluntario está disponible los días “{dia_disponible}” en el periodo de “{inicio_disponible}” a '
    '“{final_disponible}” horas'
)
def step_impl(context, dia_disponible, inicio_disponible, final_disponible):
    # Voluntario
    context.voluntario = Voluntario(
        nombre=fake.first_name(),
        apellido=fake.last_name(),
        edad=fake.pyint(min_value=18, max_value=50)
    )
    print(context.voluntario)
    context.voluntario.save()

    # Horario del voluntario
    context.horario = Horario(
        voluntario_id=context.voluntario.id
    )
    context.horario.save()

    # Periodo disponible
    context.periodo = Periodo(
        dia_semana=dia_disponible,
        hora_inicio=inicio_disponible,
        hora_fin=final_disponible,
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
        dia_semana=dia_solicitado,
        hora_inicio=inicio_solicitado,
        hora_fin=final_solicitado,
        horario_id=context.horario_solicitud.id
    )
    context.periodo_solicitud.save()


@step('se tendrá que la disponibilidad del voluntario en el momento requerido es “{disponibilidad}”')
def step_impl(context, disponibilidad):
    disponibilidad_calculada = context.voluntario.comprobar_disponibilidad(context.periodo_solicitud)
    disponibilidad_recibida = disponibilidad == "Disponible"

    assert disponibilidad_calculada == disponibilidad_recibida


@step("que el voluntario tiene un horario con sus periodos de disponibilidad")
def step_impl(context):
    context.voluntario = Voluntario(
        nombre=fake.first_name(),
        apellido=fake.last_name(),
        edad=fake.pyint(min_value=18, max_value=50)
    )
    context.voluntario.save()

    # Horario del voluntario
    context.horario = Horario(
        voluntario_id=context.voluntario.id
    )
    context.horario.save()

    # Periodos de disponibilidad
    cantidad_periodos_solicitados = random.randint(3, 15)
    for _ in range(cantidad_periodos_solicitados):
        dia_semana_faker = fake.day_of_week()
        hora_inicio_faker, _ = Periodo.str_to_time(fake.time('%H:%M'))
        hora_fin_faker, _ = Periodo.str_to_time(fake.time('%H:%M'))

        context.periodo = Periodo(
            dia_semana=dia_semana_faker,
            hora_inicio=hora_inicio_faker,
            hora_fin=hora_fin_faker,
            horario_id=context.horario.id
        )
        context.periodo.save()


@step(
    "el voluntario quiera registrar su disponibilidad los días “{dia_solicitado}” en el periodo de “{"
    "inicio_solicitado}” a “{final_solicitado}” horas")
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado):
    # Se transforman los string y se retorna un booleano si se cumplen con las condiciones indicadas en str_to_time()
    hora_inicio_solicitado, flag_inicio_correcto = Periodo.str_to_time(inicio_solicitado)
    hora_fin_solicitado, flag_fin_correcto = Periodo.str_to_time(final_solicitado)

    # Periodo solicitado
    context.periodo_solicitud = Periodo(
        dia_semana=dia_solicitado,
        hora_inicio=hora_inicio_solicitado,
        hora_fin=hora_fin_solicitado,
        horario_id=context.horario.id
    )

    # Variable booleana para determinar si la hora entregada está entre 00:00 y 23:59
    context.flag_se_registra = flag_inicio_correcto and flag_fin_correcto


@step("los datos introducidos son consistentes")
def step_impl(context):
    if context.flag_se_registra:
        # Si se procede con el registro, se comprueba la consistencia y se retorna el booleano correspondiente
        context.flag_se_registra = context.periodo_solicitud.es_consistente()


@step("el periodo introducido no tiene conflictos con otros periodos")
def step_impl(context):
    if context.flag_se_registra:
        # Si se procede con el registro, se comprueba conflictos y se retorna el booleano correspondiente
        context.flag_se_registra = context.periodo_solicitud.no_tiene_conflicto()


@step("se registrará el periodo solicitado")
def step_impl(context):
    if context.flag_se_registra:
        # Después de haber comprobado las condiciones de registro del periodo se guarda en la base de datos
        context.periodo_solicitud.save()

    periodos_registrados = Periodo.obtener_periodos_por_id_horario(context.horario.id)
    assert (context.periodo_solicitud in periodos_registrados) == context.flag_se_registra
