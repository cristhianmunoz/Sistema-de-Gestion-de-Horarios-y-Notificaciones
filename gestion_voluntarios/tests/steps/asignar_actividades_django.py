import os

from behave import *
from gestion_voluntarios.models import Emergencia, Actividad, Voluntario

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

use_step_matcher("parse")


# Sirve para verificar .feature y este .py


@step('que se tiene una emergencia con un "{nombre_emergencia}" que aún no es atendida')
def step_impl(context, nombre_emergencia):
    # Se crea la Emergencia
    context.emergenciaTest = Emergencia(nombre=nombre_emergencia)
    context.emergenciaTest.save()
    print('Emergencia Creada')
    print(context.emergenciaTest.__str__())


@step(
    'hay un voluntario con un "{nombre_voluntario}", "{apellido_voluntario}" y "{edad_voluntario}" que asistirá sin '
    'actividades asignadas')
def step_impl(context, nombre_voluntario, apellido_voluntario, edad_voluntario):
    # Se crea el voluntario
    context.voluntarioTest = Voluntario(nombre=nombre_voluntario, apellido=apellido_voluntario, edad=edad_voluntario,
                                        emergencia=context.emergenciaTest)
    context.voluntarioTest.save()
    print('Voluntario Creado')
    print(context.voluntarioTest.__str__())


@step('existe una actividad con un "{nombre_actividad}" sin voluntarios asignados')
def step_impl(context, nombre_actividad):
    # Se crea la actividad
    context.actividadTest = Actividad(nombre=nombre_actividad, emergencia=context.emergenciaTest)
    context.actividadTest.save()
    print('Actividad Creada')
    print(context.actividadTest.__str__())

    # Creamos la actividad y voluntario dentro de la Emergencia
    # Tomar en cuenta que las listas
    context.emergenciaTest.add_voluntarios(context.voluntarioTest)
    context.emergenciaTest.add_actividades(context.actividadTest)
    print(context.emergenciaTest.__str__())


@step("se le asigna un voluntario a una actividad existente")
def step_impl(context):
    # Se asigna un voluntario a una actividad
    context.actividadTest.asignar_voluntario(context.voluntarioTest)

    print('Actividad asignada a voluntario')
    print(context.actividadTest.__str__())

    # Se verifica que dentro de la emergencia los voluntarios y actividades cambien su bandera
    context.emergenciaTest.verificar_emergencia()


@step('el estado de voluntario sera"{es_asignado}"')
def step_impl(context, es_asignado):
    resultado = context.voluntarioTest.get_es_asignado()
    assert resultado == es_asignado, "No pasa el step"
    print('Estado de Voluntario correcto')


@step('el estado de la actividad sera"{tiene_voluntario}"')
def step_impl(context, tiene_voluntario):
    resultado = context.actividadTest.get_tiene_voluntario()
    assert resultado == tiene_voluntario, "No pasa el step"
    print('Estado de Actividad correcto')


@step('el estado de la emergencia sera"{estado_emergencia}"')
def step_impl(context, estado_emergencia):
    resultado = context.emergenciaTest.get_es_atendida()
    assert resultado == estado_emergencia, "No pasa el step"
    print('Estado de Emergencia correcto')
