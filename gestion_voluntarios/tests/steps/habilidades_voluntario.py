import random

from behave import *
from faker import Faker

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")
fake = Faker('es_ES')


@step('que soy un voluntario inscrito en el programa de voluntariado de la institución médica')
def step_impl(context):
    context.voluntario = Voluntario(
        nombre=fake.first_name(),
        apellido=fake.last_name(),
        edad=fake.pyint(min_value=18, max_value=50)
    )

    context.voluntario.save()

    print('Se creó el voluntario ' + context.voluntario.nombre + ' ' + context.voluntario.apellido + '.')


@step('registre mi nueva habilidad médica en mi perfil de voluntario')
def step_impl(context):
    context.nueva_habilidad = Habilidad(
        titulo=random.choice(list(HabilidadMedica)),
        descripcion=fake.sentence(nb_words=10),
        horas_experiencia=fake.pyint(min_value=1, max_value=1000),
        voluntario_id=context.voluntario.id
    )

    Habilidad.agregar_habilidad(context.nueva_habilidad)

    print(
        'Se agregó la habilidad ' +
        context.nueva_habilidad.titulo + ' en el perfil del voluntario ' +
        context.voluntario.nombre + ' ' + context.voluntario.apellido + '.'
    )


@step('la nueva habilidad médica estará registrada en mi perfil de voluntario')
def step_impl(context):
    habilidades_registradas = Habilidad.obtener_habilidades_por_id_voluntario(context.voluntario.id)

    assert context.nueva_habilidad in habilidades_registradas

    print(
        'La habilidad ' + context.nueva_habilidad.titulo +
        ' se encuentra registrada en el perfil del voluntario ' +
        context.voluntario.nombre + ' ' + context.voluntario.apellido + '.\n'
    )


@step('Tengo registrada al menos una habilidad médica en mi perfil de voluntario')
def step_impl(context):
    context.habilidad_registrada = Habilidad(
        titulo=random.choice(list(HabilidadMedica)),
        descripcion=fake.sentence(nb_words=10),
        horas_experiencia=fake.pyint(min_value=1, max_value=1000),
        voluntario_id=context.voluntario.id
    )

    Habilidad.agregar_habilidad(context.habilidad_registrada)

    print(
        'La habilidad ' +
        context.habilidad_registrada.titulo + ' se encuentra registrada en el perfil del voluntario ' +
        context.voluntario.nombre + ' ' + context.voluntario.apellido + '.'
    )


@step('actualice la información de una de mis habilidades médicas en mi perfil de voluntario')
def step_impl(context):
    context.habilidad_actualizada = Habilidad(
        id=context.habilidad_registrada.id,
        titulo=context.habilidad_registrada.titulo,
        descripcion=fake.sentence(nb_words=10),
        horas_experiencia=fake.pyint(min_value=1, max_value=1000),
        voluntario_id=context.voluntario.id
    )

    Habilidad.editar_habilidad(context.habilidad_actualizada)

    print(
        'La habilidad ' + context.habilidad_actualizada.titulo + ' del voluntario ' +
        context.voluntario.nombre + ' ' + context.voluntario.apellido + ' ha sido actualizada.'
    )


@step("la habilidad médica será actualizada en mi perfil de voluntario")
def step_impl(context):
    habilidades_registradas = Habilidad.obtener_habilidades_por_id_voluntario(context.voluntario.id)

    assert context.habilidad_actualizada in habilidades_registradas

    print(
        'La habilidad ' + context.habilidad_actualizada.titulo + ' del voluntario ' +
        context.voluntario.nombre + ' ' + context.voluntario.apellido + ' se encuentra actualizada.'
    )
