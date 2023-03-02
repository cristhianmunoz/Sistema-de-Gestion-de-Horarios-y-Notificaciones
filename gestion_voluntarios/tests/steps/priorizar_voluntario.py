import string

from behave import *

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")


@step('que tengo una emergencia que necesita de "{vacantes:f}" voluntarios con la habilidad "{habilidad_solicitada}"')
def step_impl(context, vacantes: float, habilidad_solicitada: string):
    context.emergencia = Emergencia(float(vacantes), habilidad_solicitada)


@step('tengo a varios "{lista_voluntarios_confirmados}" que confirmaron la asistencia')
def step_impl(context, lista_voluntarios_confirmados):
    lista = eval(lista_voluntarios_confirmados)
    context.lista_voluntarios = []
    for voluntario in lista.values():
        voluntario_creado = Voluntario(voluntario["Nombre"])
        habilidad = Habilidad(voluntario=voluntario_creado, titulo=voluntario["Habilidad"], horas_experiencia=voluntario["horas_experiencia"])
        context.lista_voluntarios.append(voluntario_creado)
        context.emergencia.lista = context.lista_voluntarios
        print(context.emergencia.lista)
    context.emergencia.obtener_voluntarios_habilidad("suturar")
        # print(voluntario)


@step('deseo priorizar los voluntarios con mas experiencia según la habilidad "{habilidad_solicitada}"')
def step_impl(context, habilidad_solicitada):
    #context.emergencia.priorizar_voluntarios(context.lista_voluntarios, habilidad_solicitada)
    pass


@step('tendré una lista "{lista_voluntarios_priorizada}" priorizada')
def step_impl(context, lista_voluntarios_priorizada):
    pass
