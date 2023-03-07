from behave import *

use_step_matcher("parse")

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.controller.voluntario_controller import obtener_voluntarios_controller,nombre_voluntario,obtener_voluntario
from gestion_voluntarios.controller.emergencia_controller import solicitar_servicios_voluntarios, \
    verificar_habilidades_requeridas, obtener_nombres_voluntario, enviar_notificaciones
from gestion_voluntarios.model.habilidad_model import Habilidad


@step(
    'que tengo una emergencia medica que necesita {numero_voluntarios_requeridos}" con "{titulo}" y su descripcion es '
    '"{descripcion_emergencia}" y se necesita "{habilidades_requeridas}" para atender esa emergencia')
def step_impl(context, numero_voluntarios_requeridos, descripcion_emergencia, titulo, habilidades_requeridas):
    context.emergencia = Emergencia(numero_voluntarios_requeridos, titulo, descripcion_emergencia,
                                    habilidades_requeridas.split(","), "n", "n", "n", "n", "", "", "")
    # Se crea las habilidades de la emergencia
    assert context.emergencia.habilidades_requeridas == habilidades_requeridas.split(",")


@step('solicite servicios a los "{voluntarios}" registrados en el sistema')
def step_impl(context, voluntarios):
    voluntario_registrados_nombres = []
    for voluntario_comprobar in obtener_voluntarios_controller():
        voluntario_registrados_nombres.append(voluntario_comprobar.nombre)
    assert voluntario_registrados_nombres == voluntarios.split(",")


@step('las "{habilidades_voluntario}" "{cumple}" cumplen "{habilidades_requeridas}"')
def step_impl(context, habilidades_voluntario, cumple, habilidades_requeridas):
    context.voluntarios_filtrados = solicitar_servicios_voluntarios(obtener_voluntarios_controller(),
                                                                    context.emergencia.habilidades_requeridas)
    assert verificar_habilidades_requeridas(habilidades_voluntario, habilidades_requeridas) == cumple


@step('conseguire el filtrado con la {lista_voluntarios_seleccionados}"')
def step_impl(context, lista_voluntarios_seleccionados):
    assert obtener_nombres_voluntario(context.voluntarios_filtrados) == lista_voluntarios_seleccionados.split(",")


@step('se enviaran "{numero_de_notificaciones}" notificaciones en base a la lista de voluntarios seleccionados')
def step_impl(context, numero_de_notificaciones):
    assert enviar_notificaciones(context.voluntarios_filtrados) == int(numero_de_notificaciones)


@step("la cantidad de voluntarios seleccionados sea igual a la cantidad de voluntarios requeridos")
def step_impl(context):
    # Implementar un metodo para poder hacer la comparativa y expandirle
    assert len(context.voluntarios_filtrados) == int(context.emergencia.numero_de_voluntarios_requeridos)


@step('solicite servicios a cada "{voluntario}" registrado en el sistema')
def step_impl(context, voluntario):
    assert nombre_voluntario(obtener_voluntario()) == voluntario


@step('se selecciona al voluntario y se lo coloca en una {lista_voluntarios_seleccionados}"')
def step_impl(context, lista_voluntarios_seleccionados):

    raise NotImplementedError(
        u'STEP: Entonces se selecciona al voluntario y se lo coloca en una <lista_voluntarios_seleccionados>"')