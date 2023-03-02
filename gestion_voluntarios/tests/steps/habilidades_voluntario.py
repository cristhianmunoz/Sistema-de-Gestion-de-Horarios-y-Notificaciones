from behave import *

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")


@step(
    'que el voluntario tiene registrada “{cantidad_habilidades_registradas:f}” habilidad médica con el título '
    '“{titulo_habilidad}” con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, cantidad_habilidades_registradas, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    context.voluntario = Voluntario(
        id=1,
        nombre='Andrés',
        apellido='Lozano',
        edad=24
    )
    context.voluntario.save()

    context.habilidad = Habilidad(
        id=1,
        titulo=titulo_habilidad,
        descripcion=descripcion_habilidad,
        horas_experiencia=horas_experiencia,
        voluntario_id=context.voluntario.id
    )
    context.habilidad.save()

    assert Habilidad.obtener_numero_habilidades_por_id_voluntario(
        context.voluntario.id) == cantidad_habilidades_registradas


@step(
    'únicamente existen las habilidades médicas “{habilidad_suturar}”, “{habilidad_vacunar}” y “{habilidad_anestesiar}”'
)
def step_impl(context, habilidad_suturar, habilidad_vacunar, habilidad_anestesiar):
    assert habilidad_suturar in HabilidadMedica
    assert habilidad_vacunar in HabilidadMedica
    assert habilidad_anestesiar in HabilidadMedica


@step(
    'el voluntario intente registrar una nueva habilidad médica con el título “{titulo_habilidad}”, '
    'con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    context.habilidad = Habilidad(
        titulo=titulo_habilidad,
        descripcion=descripcion_habilidad,
        horas_experiencia=horas_experiencia,
        voluntario_id=context.voluntario.id
    )
    context.habilidad.save()


@step(
    'el voluntario tendrá registrada “{cantidad_habilidades_registradas:f}” habilidad médica con el título '
    '“{titulo_habilidad}”, con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, cantidad_habilidades_registradas, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    habilidades = Habilidad.obtener_habilidades_por_id_voluntario(context.voluntario.id)

    assert Habilidad.obtener_numero_habilidades_por_id_voluntario(
        context.voluntario.id) == cantidad_habilidades_registradas

    assert habilidades[0].titulo == titulo_habilidad
    assert habilidades[0].descripcion == descripcion_habilidad
    assert habilidades[0].horas_experiencia == horas_experiencia


@step('que el voluntario tiene registradas “{cantidad_habilidades_registradas:f}” habilidades médicas')
def step_impl(context, cantidad_habilidades_registradas):
    context.voluntario = Voluntario(
        id=2,
        nombre='Francisco',
        apellido='Encalada',
        edad=22
    )
    context.voluntario.save()

    assert Habilidad.obtener_numero_habilidades_por_id_voluntario(
        context.voluntario.id) == cantidad_habilidades_registradas


@step('el voluntario tendrá registradas “{cantidad_habilidades_registradas:f}” habilidades médicas')
def step_impl(context, cantidad_habilidades_registradas):
    assert Habilidad.obtener_numero_habilidades_por_id_voluntario(
        context.voluntario.id) == cantidad_habilidades_registradas


@step(
    'el voluntario tendrá registrada “{cantidad_habilidades_registradas:f}” habilidad médica registrada con el título '
    '“{titulo_habilidad}”, con “{horas_experiencia:f}” horas de experiencia y la descripción “{descripcion_habilidad}”'
)
def step_impl(context, cantidad_habilidades_registradas, titulo_habilidad, horas_experiencia, descripcion_habilidad):
    habilidades = Habilidad.obtener_habilidades_por_id_voluntario(context.voluntario.id)

    assert Habilidad.obtener_numero_habilidades_por_id_voluntario(
        context.voluntario.id) == cantidad_habilidades_registradas

    assert habilidades[0].titulo == titulo_habilidad
    assert habilidades[0].descripcion == descripcion_habilidad
    assert habilidades[0].horas_experiencia == horas_experiencia
