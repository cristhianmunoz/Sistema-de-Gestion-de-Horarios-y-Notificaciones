from behave import *
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("re")

voluntario = Voluntario("Juan", "Zuares", 23)

@step('que tengo un voluntario llamado "Juan" con las habilidades necesarias para atender la emergencia')
def step_impl(context):
    context.voluntario = voluntario
    assert context.voluntario.nombre == "Juan"


@step('Juan tiene disponibilidad el día "jueves" de "11:00" hasta "13:00"')
def step_impl(context):
    context.voluntario.comprobar_disponibilidad()

    raise NotImplementedError(u'STEP: Y Juan tiene disponibilidad el día "jueves" de "11:00" hasta "13:00"')


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


@step("que tengo un personal médico que ha informado de una ausencia imprevista en el horario de 12:00 hasta 16:00")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Dado que tengo un personal médico que ha informado de una ausencia imprevista en el horario de 12:00 hasta 16:00')


@step("necesito encontrar uno o mas voluntario para cubrir su turno en ese horario")
def step_impl(context):
    raise NotImplementedError(u'STEP: Y necesito encontrar uno o mas voluntario para cubrir su turno en ese horario')


@step("el administrador del personal médico busca los voluntario disponible para cubrir el turno")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Cuando el administrador del personal médico busca los voluntario disponible para cubrir el turno')


@step("el sistema muestra una lista de voluntarios disponibles y con las habilidades necesarias")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Entonces el sistema muestra una lista de voluntarios disponibles y con las habilidades necesarias')


@step("el administrador del personal médico selecciona uno o mas voluntarios adecuado y lo asigna para cubrir el turno")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Y el administrador del personal médico selecciona uno o mas voluntarios adecuado y lo asigna para cubrir el turno')


@step("el sistema actualiza automáticamente el horario del voluntario seleccionado")
def step_impl(context):
    raise NotImplementedError(u'STEP: Y el sistema actualiza automáticamente el horario del voluntario seleccionado')