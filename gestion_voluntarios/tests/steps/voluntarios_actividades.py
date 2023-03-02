import datetime

from behave import *
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.periodo_model import Periodo

use_step_matcher("re")

voluntario = Voluntario("Juan", "Zuares", 23)

@step('que tengo un voluntario llamado "Juan" con las habilidades necesarias para atender la emergencia')
def step_impl(context):
    context.voluntario = voluntario
    assert context.voluntario.nombre == "Juan"


@step('Juan tiene disponibilidad el día "jueves" de "11:00" hasta "13:00"')
def step_impl(context):
    context.periodo = Periodo(horaInicio=datetime.time(11, 0), horaFin=datetime.time(13, 0))
    isDisponible = context.voluntario.comprobar_disponibilidad(context.periodo)
    assert isDisponible

@step('se presenta una emergencia el día "jueves" a las "12:00"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Y se presenta una emergencia el día "jueves" a las "12:00"')


@step("el administrador del personal médico asigna a Juan para atender la emergencia")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Cuando el administrador del personal médico asigna a Juan para atender la emergencia')


@step("el sistema actualiza automáticamente el horario de Juan")
def step_impl(context):
    raise NotImplementedError(u'STEP: Entonces el sistema actualiza automáticamente el horario de Juan')


@step("Juan recibe una notificación sobre su participación en la emergencia")
def step_impl(context):
    raise NotImplementedError(u'STEP: Y Juan recibe una notificación sobre su participación en la emergencia')
