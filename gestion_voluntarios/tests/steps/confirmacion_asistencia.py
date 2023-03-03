import django
import os

from behave import *

django.setup()

from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.controller.voluntario_notificacion_controller import obtener_voluntarios_confirmados, \
    contar_elementos, obtener_nombres

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

use_step_matcher("parse")


@step("que se tiene el grupo de voluntarios conformado por '{lista_voluntarios}'")
def step_impl(context, lista_voluntarios):
    """
        :type context: behave.runner.Context
    """
    context.lista_voluntarios = [Voluntario('Juan', 'Pérez', 30, 'Sutura', 'D'),
                                 Voluntario('Pepe', 'Rodríguez', 35, 'Primeros Auxilios', 'D'),
                                 Voluntario('Tomás', 'Muenala', 40, 'Sutura', 'D'),
                                 Voluntario('Ana', 'Freire', 25, 'Sutura', 'O'),
                                 Voluntario('Gerardo', 'Zapata', 23, 'Sutura', 'O')]
    aux_lista = obtener_nombres(context.lista_voluntarios)
    assert aux_lista == lista_voluntarios

    # raise NotImplementedError(u'STEP: 'Dado que soy un voluntario registrado en el programa de emergencia médica')


@step("se notifica la emergencia médica a '{n:d}' personas")
def step_impl(context, n):
    """
    :type context: behave.runner.Context
    """
    context.numero = contar_elementos(context.lista_voluntarios)
    assert context.numero == n
    # print("n: ", context.numero)
    # raise NotImplementedError(u'STEP: Cuando recibo una notificación de emergencia')


@step("el numero de voluntarios que confirmaron su asistencia es '{numero_confirmados:d}'")
def step_impl(context, numero_confirmados):
    """
    :type context: behave.runner.Context
    """
    # print(context.lista_voluntarios)
    # print(obtener_voluntarios_confirmados(context.lista_voluntarios))
    context.numero_confirmados = contar_elementos(obtener_voluntarios_confirmados(context.lista_voluntarios))
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
    # raise NotImplementedError(u'STEP: Entonces mi asistencia es registrada en el sistema')


@step("los voluntarios asignados a esta emergencia son '{lista_confirmados}'")
def step_impl(context, lista_confirmados):
    """
    :type context: behave.runner.Context
    """
    # print(context.lista_voluntarios)
    context.list_confirmados = obtener_voluntarios_confirmados(context.lista_voluntarios)
    aux_voluntarios = obtener_nombres(context.list_confirmados)
    # print("a", lista_confirmados)
    # print("b", aux_voluntarios)
    assert aux_voluntarios == lista_confirmados
    # print(context.lista_confirmados)
    # raise NotImplementedError(u'STEP: Y se me notifica mi asignación en la emergencia médica')
