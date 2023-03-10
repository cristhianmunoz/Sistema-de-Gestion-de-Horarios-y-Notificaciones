import os

from behave import *
from faker import Faker

from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.actividad_model import Actividad
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

faker = Faker("es_ES")

use_step_matcher("parse")


@step('que se tiene una emergencia que aún no es atendida')
def step_impl(context):
    # Se crea la Emergencia
    nombre_emergencia = faker.name()
    context.emergenciaTest = Emergencia(nombre=nombre_emergencia)
    context.emergenciaTest.save()


@step('hay una "{cantidad_voluntarios}" que asistirán sin actividades asignadas')
def step_impl(context, cantidad_voluntarios):
    # Uso de la cantidad de voluntarios
    cantidad_voluntarios_int = int(cantidad_voluntarios)
    # Se crean voluntarios con ayuda de la cantidad
    for i in range(cantidad_voluntarios_int):
        # Creación de los voluntarios
        nombre_voluntario = faker.first_name()
        apellido_voluntarios = faker.last_name()
        edad_voluntario = faker.random_int(min=0, max=100)
        context.voluntarioTest = Voluntario(nombre=nombre_voluntario,
                                            apellido=apellido_voluntarios,
                                            edad=edad_voluntario,
                                            emergencia=context.emergenciaTest)
        context.voluntarioTest.save()
        # Añadimos voluntarios en la Emergencia
        context.emergenciaTest.add_voluntarios(context.voluntarioTest)


@step('existe una actividad con un "{nombre_actividad}" sin voluntarios asignados')
def step_impl(context, nombre_actividad):
    # Se crea la actividad
    context.actividadTest = Actividad(nombre=nombre_actividad,
                                      emergencia=context.emergenciaTest)
    context.actividadTest.save()

    # Añadimos la actividad en la Emergencia
    context.emergenciaTest.add_actividades(context.actividadTest)

    context.emergenciaTest.save()


@step('se le asigna voluntarios a una actividad existente')
def step_impl(context):
    # Obtenga los voluntarios
    lista_voluntarios = context.emergenciaTest.get_voluntarios()
    # Asignamos voluntarios a la actividad
    for voluntario in lista_voluntarios:
        context.actividadTest.asignar_voluntario(voluntario)
        context.actividadTest.save()
        voluntario.save()

    context.emergenciaTest.save()

    # Se verifica que dentro de la emergencia los voluntarios y actividades cambien su bandera
    context.emergenciaTest.verificar_emergencia()
    context.emergenciaTest.save()


@step('el estado de voluntario sera"{es_asignado}"')
def step_impl(context, es_asignado):
    # Se verifica los valores dentro de emergencia
    lista_vol = context.emergenciaTest.get_voluntarios()
    for voluntario in lista_vol:
        resultado = str(voluntario.get_es_asignado())
        assert resultado == es_asignado, "No pasa el step"


@step('el estado de la actividad sera"{tiene_voluntario}"')
def step_impl(context, tiene_voluntario):
    resultado = str(context.actividadTest.get_tiene_voluntario())
    assert resultado == tiene_voluntario, "No pasa el step"


@step('el estado de la emergencia sera"{estado_emergencia}"')
def step_impl(context, estado_emergencia):
    resultado = str(context.emergenciaTest.get_es_atendida())
    assert resultado == estado_emergencia, "No pasa el step"

    # Borrar registros creados dentro de la base de datos
    lista_vol = context.emergenciaTest.get_voluntarios()
    for v in lista_vol:
        v.delete()

    lista_vol_act = context.actividadTest.get_voluntarios()
    for va in lista_vol_act:
        va.delete()

    context.emergenciaTest.delete()







