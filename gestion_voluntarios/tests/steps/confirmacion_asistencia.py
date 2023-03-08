import django
import os
import datetime
import random

from behave import *
from faker import Faker

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.controller.voluntario_notificacion_controller import obtener_voluntarios_confirmados, \
    contar_elementos, obtener_nombres

django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

faker = Faker("es_ES")

use_step_matcher("parse")


@step("que se tiene el grupo de '{n:d}' voluntarios")
def step_impl(context, n):
    """
        :type context: behave.runner.Context
    """
    nombre_emergencia = faker.name()
    asunto = faker.sentence()
    ubicacion = faker.city()
    hora_entrada = datetime.time(hour=random.randint(7, 9), minute=random.randint(0, 59))
    # esta hora debe empatar con el horario de los voluntarios
    num_voluntarios = int(n)
    es_atendida = True

    context.mi_emergencia = Emergencia(nombre=nombre_emergencia,
                                       asunto=asunto,
                                       ubicacion=ubicacion,
                                       hora_entrada=hora_entrada,
                                       num_voluntarios_necesarios=num_voluntarios,
                                       es_atendida=es_atendida)
    context.mi_emergencia.save()
    context.lista_voluntarios_general = []
    for i in range(context.mi_emergencia.num_voluntarios_necesarios):
        # Creación de los voluntarios
        nombre_voluntario = faker.first_name()
        apellido_voluntario = faker.last_name()
        edad_voluntario = faker.random_int(min=0, max=100)
        estado = 'D'
        es_asignado = False
        context.mi_voluntario = Voluntario(nombre=nombre_voluntario,
                                           apellido=apellido_voluntario,
                                           edad=edad_voluntario,
                                           estado=estado,
                                           es_asignado=es_asignado,
                                           emergencia=context.mi_emergencia)
        context.mi_voluntario.save()
        # Añadimos voluntarios a la lista
        context.lista_voluntarios_general.append(context.mi_voluntario)
        # Añadimos voluntarios en la Emergencia
        # Esta funcionalidad la hace el GRUPO 3 cuando asigne actividades
        # context.mi_emergencia.add_voluntarios(context.mi_voluntario)

    # raise NotImplementedError(u'STEP: 'Dado que soy un voluntario registrado en el programa de emergencia médica')


@step("se notifica la emergencia médica a este grupo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # lógica de la confirmación
    for voluntario in context.lista_voluntarios_general:
        voluntario.confirmar_asistencia()


    # raise NotImplementedError(u'STEP: Cuando recibo una notificación de emergencia')


@step("el numero de voluntarios que confirmaron su asistencia es '{numero_confirmados:d}'")
def step_impl(context, numero_confirmados):
    """
    :type context: behave.runner.Context
    """
    # print(context.lista_voluntarios)
    # print(obtener_voluntarios_confirmados(context.lista_voluntarios))
    context.lista_confirmados = obtener_voluntarios_confirmados(context.lista_voluntarios_general)
    context.numero_confirmados = contar_elementos(context.lista_confirmados)
    # print("n confirmados: ", context.numero_confirmados)
    assert numero_confirmados == context.numero_confirmados
    # print(context.numero_confirmados)
    # raise NotImplementedError(u'STEP: Y selecciono la opción "Confirmar"')


@step("el numero de voluntarios que rechazaron la emergencia es '{numero_rechazados:d}'")
def step_impl(context, numero_rechazados):
    """
    :type context: behave.runner.Context
    """
    context.num_rechazados = context.numero - context.numero_confirmados
    # assert context.num_rechazados == numero_rechazados
    # print(context.num_rechazados)
    # print(contar_elementos(obtener_voluntarios_rechazados(context.lista_voluntarios)))

    # raise NotImplementedError(u'STEP: Y selecciono la opción "Confirmar"')


@step("el número de voluntarios que atenderán la emergencia es '{numero_confirmados:d}'")
def step_impl(context, numero_confirmados):
    """
        :type context: behave.runner.Context
    """
    for voluntario in context.lista_confirmados:
        print(voluntario.to_string())
    # raise NotImplementedError(u'STEP: Entonces mi asistencia es registrada en el sistema')
