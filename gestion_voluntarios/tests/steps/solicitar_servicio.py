import django
import os
import datetime
import random

from faker import Faker
from behave import *

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")
faker = Faker("es_ES")

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.controller.voluntario_controller import obtener_voluntarios_controller
from gestion_voluntarios.controller.emergencia_controller import solicitar_servicios_voluntarios, \
    verificar_habilidades_requeridas, obtener_nombres_voluntario, enviar_notificaciones, \
    voluntarios_seleccionados, seleccionar_voluntarios
from gestion_voluntarios.model.habilidad_model import Habilidad


@step(
    'que tengo una emergencia medica que necesita {num_voluntarios_necesarios}" con "{nombre}" y su descripcion es "{'
    'asunto}" y se necesita "{habilidad_requerida}" para atender esa emergencia')
def step_impl(context, num_voluntarios_necesarios, nombre, asunto, habilidad_requerida):
    context.emergenciaTest = Emergencia(
        num_voluntarios_necesarios=num_voluntarios_necesarios,
        nombre=nombre,
        asunto=asunto,
        habilidad_requerida=habilidad_requerida
    )
    context.emergenciaTest.save()


@step('solicite servicios a los "{voluntarios}" registrados en el sistema')
def step_impl(context, voluntarios):
    # Simular una creacion de voluntarios
    context.numero_voluntarios = len(voluntarios.split(","))
    for i in range(context.numero_voluntarios):
        context.voluntarioTest = Voluntario(
            nombre=voluntarios.split(",")[i],
            edad=faker.random_int(min=18, max=60)
        )
        context.voluntarioTest.save()

        nueva_habilidad = Habilidad(
            titulo=random.choice(list(HabilidadMedica)),
            descripcion=faker.sentence(nb_words=10),
            horas_experiencia=faker.pyint(min_value=1, max_value=1000),
            voluntario_id=context.voluntarioTest.id
        )
        Habilidad.agregar_habilidad(nueva_habilidad)


@step('las "{habilidades_voluntario}" "{cumple}" cumplen "{habilidades_requeridas}"')
def step_impl(context, habilidades_voluntario, cumple, habilidades_requeridas):
    context.voluntarios_filtrados = solicitar_servicios_voluntarios(obtener_voluntarios_controller(),
                                                                    context.emergencia.habilidades_requeridas)
    assert verificar_habilidades_requeridas(habilidades_voluntario, habilidades_requeridas) == cumple


@step('conseguire el filtrado con la {lista_voluntarios_seleccionados}"')
def step_impl(context, lista_voluntarios_seleccionados):
    assert obtener_nombres_voluntario(context.voluntarios_filtrados) == lista_voluntarios_seleccionados.split(",")


@step('se enviaran "{numero_de_notificaciones}" notificaciones en base a la lista de voluntarios seleccionados')
def step_impl(context, numero_de_notificaciones):
    assert enviar_notificaciones(context.voluntarios_filtrados) == int(numero_de_notificaciones)


@step("la cantidad de voluntarios seleccionados sea igual a la cantidad de voluntarios requeridos")
def step_impl(context):
    # Implementar un metodo para poder hacer la comparativa y expandirle
    assert len(context.voluntarios_filtrados) == int(context.emergencia.numero_de_voluntarios_requeridos)


@step('si el numero de "{voluntario_seleccionado}" es igual al "{numero_voluntarios_requeridos}"')
def step_impl(context, voluntario_seleccionado, numero_voluntarios_requeridos):
    context.voluntarios_seleccionados_final = voluntarios_seleccionados(context.voluntarios_ordenados,
                                                                        int(numero_voluntarios_requeridos))
    assert len(context.voluntarios_seleccionados_final) == int(numero_voluntarios_requeridos)


@step('se enviaran "{numero_de_notificaciones}" notificaciones a la lista de "{voluntarios_seleccionados}"')
def step_impl(context, numero_de_notificaciones, voluntarios_seleccionados):
    # complementar con el método que me da la lista de voluntarioa
    assert enviar_notificaciones(context.voluntarios_seleccionados_final) == int(numero_de_notificaciones)


@step(
    'consiga la "{lista_voluntarios_ordenados}" de mayor a menor segun el número de habilidades del voluntario que '
    'cumplen de la habilidad requerida"')
def step_impl(context, lista_voluntarios_ordenados):
    # Los voluntarios de la base de datos
    context.habilidad_requerida_emergencia = Emergencia.habilidad_requerida
    seleccionar_voluntarios(context.habilidad_requerida_emergencia)

    pass
