import os

from behave import *

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

use_step_matcher("parse")


@step("que se tiene el grupo de voluntarios conformado por {lista_voluntarios}")
def step_impl(context, lista_voluntarios):
    """
        :type context: behave.runner.Context
    """
    context.lista_voluntarios = [Voluntario('Juan', 'Pérez', 30, 'Sutura', True),
                                 Voluntario('Pepe', 'Rodríguez', 35, 'Primeros Auxilios', True),
                                 Voluntario('Tomás', 'Muenala', 40, 'Sutura', True),
                                 Voluntario('Ana', 'Freire', 25, 'Sutura', True),
                                 Voluntario('Gerardo', 'Zapata', 23, 'Sutura', True)]
    # raise NotImplementedError(u'STEP: 'Dado que soy un voluntario registrado en el programa de emergencia médica')


@step("se notifica la emergencia médica a {n} personas")
def step_impl(context, n):
    """
    :type context: behave.runner.Context
    """
    context.n = context.lista_voluntarios.size()
    # raise NotImplementedError(u'STEP: Cuando recibo una notificación de emergencia')


@step('el numero de voluntarios que confirmaron su asistencia es {n_c}')
def step_impl(context, n_c):
    """
    :type context: behave.runner.Context
    """


    # raise NotImplementedError(u'STEP: Y selecciono la opción "Confirmar"')


@step('el numero de voluntarios que rechazaron la emergencia es {n_r}')
def step_impl(context, n_r):
    """
    :type context: behave.runner.Context
    """


    # raise NotImplementedError(u'STEP: Y selecciono la opción "Confirmar"')


@step("el número de voluntarios que atenderán la {emergencia} es {n_c}")
def step_impl(context, emergencia, n_c):
    """
        :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Entonces mi asistencia es registrada en el sistema')


@step("los voluntarios asignados a esta emergencia son {lista_confirmados}")
def step_impl(context, lista_confirmados):
    """
    :type context: behave.runner.Context
    """


    # raise NotImplementedError(u'STEP: Y se me notifica mi asignación en la emergencia médica')
