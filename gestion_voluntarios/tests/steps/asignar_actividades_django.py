import os

from behave import *
from faker import Faker

from gestion_voluntarios.models import Emergencia, Actividad, Voluntario

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

faker = Faker("es_ES")

use_step_matcher("parse")


# Sirve para verificar .feature y este .py


@step('que se tiene una emergencia que aún no es atendida')
def step_impl(context):
    # Se crea la Emergencia
    id_emergencia = faker.pystr(max_chars=10)
    nombre_emergencia = faker.name()
    context.emergenciaTest = Emergencia(id=id_emergencia, nombre=nombre_emergencia)
    context.emergenciaTest.save()
    print('Emergencia Creada')
    print(context.emergenciaTest.__str__())


@step(
    'hay un voluntario que asistirá sin actividades asignadas')
def step_impl(context):
    # Se crea el voluntario
    id_voluntario = faker.pystr(max_chars=10)
    nombre_voluntario = faker.name()
    context.voluntarioTest = Voluntario(id=id_voluntario, nombre=nombre_voluntario, emergencia=context.emergenciaTest)
    context.voluntarioTest.save()
    print('Voluntario Creado')
    print(context.voluntarioTest.__str__())


@step('existe una actividad con un "{nombre_actividad}" sin voluntarios asignados')
def step_impl(context, nombre_actividad):
    # Se crea la actividad
    id_actividad = faker.random_int(min=0, max=1000)
    context.actividadTest = Actividad(id=id_actividad, nombre=nombre_actividad, emergencia=context.emergenciaTest)
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
    context.actividadTest.save()
    context.voluntarioTest.save()
    print('Voluntario asignado a actividad')
    print(context.actividadTest.__str__())

    # Se verifica que dentro de la emergencia los voluntarios y actividades cambien su bandera
    context.emergenciaTest.verificar_emergencia()
    context.emergenciaTest.save()
    print(context.emergenciaTest.__str__())


@step('el estado de voluntario sera"{es_asignado}"')
def step_impl(context, es_asignado):
    # Se realiza la conversión de str a boolean del test
    aux = bool(es_asignado)
    resultado = context.voluntarioTest.get_es_asignado()
    assert resultado == aux, "No pasa el step"
    print('Estado de Voluntario correcto')


@step('el estado de la actividad sera"{tiene_voluntario}"')
def step_impl(context, tiene_voluntario):
    # Se realiza la conversión de str a boolean del test
    tiene_voluntario_boolean = bool(tiene_voluntario)
    resultado = context.actividadTest.get_tiene_voluntario()
    assert resultado == tiene_voluntario_boolean, "No pasa el step"
    print('Estado de Actividad correcto')


@step('el estado de la emergencia sera"{estado_emergencia}"')
def step_impl(context, estado_emergencia):
    # Se realiza la conversión de str a boolean del test
    estado_emergencia_boolean = bool(estado_emergencia)
    resultado = context.emergenciaTest.get_es_atendida()
    assert resultado == estado_emergencia_boolean, "No pasa el step"
    print('Estado de Emergencia correcto')
