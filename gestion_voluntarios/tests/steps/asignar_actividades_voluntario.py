from behave import *
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.actividad_model import Actividad

use_step_matcher("parse") #Sirve para matchear .feature y este .py


@step('que se tiene una emergencia con "{nombre_emergencia}" que aún no es atendida')
def step_impl(context, nombre_emergencia):
    context.emergenciaTest = Emergencia(nombre_emergencia)
    print('Emergencia Creada')


@step('hay un voluntario con "{nombre_voluntario}", "{apellido_voluntario}" y "{edad_voluntario}" que asistirá sin actividades asignadas')
def step_impl(context, nombre_voluntario, apellido_voluntario, edad_voluntario):
    context.voluntarioTest = Voluntario(nombre_voluntario, apellido_voluntario, edad_voluntario, '0', context.emergenciaTest)
    print('Voluntario Creado')

@step('existe una actividad con "{nombre_actividad}"')
def step_impl(context, nombre_actividad):
    context.actividadTest = Actividad(nombre_actividad, '0', context.emergenciaTest)
    print('Actividad Creada')

@step('se les asigna al menos una actividad diferente a cada voluntario')
def step_impl(context):
    context.actividadTest.asignar_actividad(context.voluntarioTest)
    context.emergenciaTest.verificar_emergencia()
    print('Actividad asiganda a voluntario')

@step('el estado de la emergencia sera "{estado_emergencia}"')
def step_impl(context, estado_emergencia):
    resultado = context.emergenciaTest.get_es_atendida()
    assert resultado == estado_emergencia, "No pasa el step de la emergencia"

@step('estado de voluntario sera "{tiene_actividad}"')
def step_impl(context, tiene_actividad):
    resultado = context.voluntarioTest.get_tiene_actividad()
    assert resultado == tiene_actividad, "No pasa el step de la emergencia"

@step('el estado de la actividad sera "{es_asignada}"')
def step_impl(context, es_asignada):
    resultado = context.actividadTest.get_es_asignada()
    assert resultado == es_asignada, "No pasa el step de la emergencia"
