import random

from faker import Faker
from behave import *

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")
faker = Faker("es_ES")

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.controller.emergencia_controller import solicitar_servicios_voluntarios, \
    obtener_voluntarios_finales, enviar_notificaciones, obtener_nombres_voluntario, enviar_notificaciones_exitosas
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
    # Creacion de voluntarios de prueba
    context.numero_voluntarios = len(voluntarios.split(","))

    lista = eval(voluntarios)
    lista_voluntarios = []
    i = 0
    for voluntario in lista.values():
        voluntario_creado = Voluntario(
            nombre=voluntario["nombre"],
            edad=faker.random_int(min=18, max=60)
        )
        voluntario_creado.save()

        for habilidad in voluntario["habilidad"]:
            habilidad_voluntario = Habilidad(
                titulo=habilidad,
                descripcion=faker.text(max_nb_chars=200),
                horas_experiencia=faker.pyint(min_value=1, max_value=1000),
                voluntario_id=voluntario_creado.id
            )
            habilidad_voluntario.save()
        lista_voluntarios.append(voluntario_creado)




    """
    for i in range(context.numero_voluntarios):
        context.voluntarioTest = Voluntario(
            nombre=voluntarios.split(",")[i],
            edad=faker.random_int(min=18, max=60)
        )
        context.voluntarioTest.save()

        context.habilidad = Habilidad(
            titulo=HabilidadMedica.ANESTESIAR,
            descripcion=faker.sentence(nb_words=10),
            horas_experiencia=faker.pyint(min_value=1, max_value=1000),
            voluntario_id=context.voluntarioTest.id
        )
        Habilidad.agregar_habilidad(context.habilidad)
        context.habilidad = Habilidad(
            titulo=HabilidadMedica.SUTURAR,
            descripcion=faker.sentence(nb_words=10),
            horas_experiencia=faker.pyint(min_value=1, max_value=1000),
            voluntario_id=context.voluntarioTest.id
        )
        Habilidad.agregar_habilidad(context.habilidad)
"""
    """
    # Creacion y asignacion de habilidades_prueba en los voluntarios_prueba
    for i in range(context.numero_voluntarios):
        context.nueva_habilidad = Habilidad(
            titulo=random.choice(list(HabilidadMedica)),
            descripcion=faker.sentence(nb_words=10),
            horas_experiencia=faker.pyint(min_value=1, max_value=1000),
            voluntario_id=faker.pyint(min_value=1, max_value=4)
        )
        Habilidad.agregar_habilidad(context.nueva_habilidad)
    """

    # Se envia a cada uno de los voluntarios y se realiza el filtrado
    context.voluntarios_db = Voluntario.get_voluntarios()
    assert obtener_nombres_voluntario(context.voluntarios_db) == obtener_nombres_voluntario(lista_voluntarios)
    context.voluntarios_seleccionados = solicitar_servicios_voluntarios(context.voluntarios_db,
                                                                        context.emergenciaTest)


@step('si el numero de "{voluntario_seleccionado}" es mayor o igual al "{num_voluntarios_necesarios}"')
def step_impl(context, voluntario_seleccionado, num_voluntarios_necesarios):
    #context.voluntarios_finales = obtener_voluntarios_finales(context.voluntarios_seleccionados,
    #                                                          int(num_voluntarios_necesarios))
    #assert obtener_nombres_voluntario(context.voluntarios_finales) == voluntario_seleccionado.split(",")
    assert len(context.voluntarios_seleccionados) >= int(num_voluntarios_necesarios)


@step('se enviaran "{numero_de_notificaciones}" notificaciones a la lista de voluntarios finales')
def step_impl(context, numero_de_notificaciones):
    assert enviar_notificaciones(context.voluntarios_seleccionados) >= int(numero_de_notificaciones)

    # BORRAR BASE DE DATOS
    lista_vol = Voluntario.get_voluntarios()
    for v in lista_vol:
        v.delete()

    lista_habilidades = Habilidad.get_habilidades()
    for va in lista_habilidades:
        va.delete()
    context.emergenciaTest.delete()


@step('si el numero de "{voluntario_seleccionado}" es menor al "{num_voluntarios_necesarios}"')
def step_impl(context, voluntario_seleccionado, num_voluntarios_necesarios):
    #context.voluntarios_finales = obtener_voluntarios_finales(context.voluntarios_seleccionados,
    #                                                          int(num_voluntarios_necesarios))
    assert len(context.voluntarios_seleccionados) < int(num_voluntarios_necesarios)


@step('se enviara unicamente "{numero_de_notificaciones_exitosas}" a la lista de voluntarios finales')
def step_impl(context, numero_de_notificaciones_exitosas):

    assert enviar_notificaciones_exitosas(context.voluntarios_seleccionados) == int(numero_de_notificaciones_exitosas)