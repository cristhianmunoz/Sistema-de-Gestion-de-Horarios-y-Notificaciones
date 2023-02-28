from behave import *

from gestion_voluntarios.models.models import Emergencia, Voluntario

use_step_matcher("parse")


@step("que yo, {nombre:S} {apellido:S}, soy un voluntario registrado en el programa de emergencia médica")
def step_impl(context, nombre, apellido):
    """
        :type context: behave.runner.Context
    """
    context.voluntario = Voluntario(nombre, apellido, 30, 'Sutura')
    # raise NotImplementedError(u'STEP: 'Dado que soy un voluntario registrado en el programa de emergencia médica')


@step("recibo una notificación informándome de una emergencia que contiene los siguientes datos '{asunto}', "
      "'{tipo_emergencia}', '{ubicacion}', '{hora_entrada}', '{encargado}', "
      "'{dirigido_a}', '{actividades}' y '{detalle}'")
def step_impl(context, asunto, tipo_emergencia, ubicacion, hora_entrada, encargado, dirigido_a, actividades, detalle):
    """
    :type context: behave.runner.Context
    """
    context.mi_emergencia = Emergencia(asunto, tipo_emergencia, ubicacion, hora_entrada, encargado, dirigido_a, actividades, detalle, True)
    # raise NotImplementedError(u'STEP: Cuando recibo una notificación de emergencia')


@step('selecciono la opción {deseada:S}')
def step_impl(context, deseada):
    """
    :type context: behave.runner.Context
    """
    if deseada != '\'Confirmar\'':
        context.mi_emergencia.respuesta = False
        #print(context.mi_emergencia.respuesta)
    else:
        context.mi_emergencia.respuesta = True
        #print(context.mi_emergencia.respuesta)


    # raise NotImplementedError(u'STEP: Y selecciono la opción "Confirmar"')


@step("la opción escogida se registra en el sistema")
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Entonces mi asistencia es registrada en el sistema')


@step("se me informa que {mensaje}")
def step_impl(context, mensaje):
    """
    :type context: behave.runner.Context
    """
    context.aviso = context.voluntario.respuesta(context.mi_emergencia.respuesta)
    assert F'\'{context.aviso}\'' == mensaje

    # raise NotImplementedError(u'STEP: Y se me notifica mi asignación en la emergencia médica')