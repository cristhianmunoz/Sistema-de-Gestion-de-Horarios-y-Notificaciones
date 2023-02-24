from behave import *

use_step_matcher("parse")


@step("que soy un voluntario registrado en el programa de emergencia médica")
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: 'Dado que soy un voluntario registrado en el programa de emergencia médica')


@step("recibo una notificación de emergencia")
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Cuando recibo una notificación de emergencia')


@step('selecciono la opción "Confirmar"')
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Y selecciono la opción "Confirmar"')


@step("mi asistencia es registrada en el sistema")
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Entonces mi asistencia es registrada en el sistema')


@step("se me notifica mi asignación en la emergencia médica")
def step_impl(context):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Y se me notifica mi asignación en la emergencia médica')
