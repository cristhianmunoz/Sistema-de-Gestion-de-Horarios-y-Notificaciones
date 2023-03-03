from behave import *

from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")


@step('que tengo una emergencia que necesita de "{vacantes:f}" voluntarios con la habilidad "{habilidad_solicitada}"')
def step_impl(context, vacantes, habilidad_solicitada):
    from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
    context.emergencia = Emergencia(
            vacantes=float(vacantes),
            habilidad_requerida=HabilidadMedica.SUTURAR
        )
    context.emergencia.save()


@step('tengo a varios "{lista_voluntarios_confirmados}" que confirmaron la asistencia')
def step_impl(context, lista_voluntarios_confirmados):
    lista = eval(lista_voluntarios_confirmados)
    lista_voluntarios = []

    for voluntario in lista.values():
        voluntario_creado = Voluntario(
            nombre=voluntario["nombre"],
            apellido=voluntario["apellido"],
            edad=voluntario["edad"]
        )
        voluntario_creado.save()

        from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica
        context.habilidad = Habilidad(
            titulo=HabilidadMedica.SUTURAR,
            descripcion="",
            horas_experiencia=voluntario["horas_experiencia"],
            voluntario_id=voluntario_creado.id
        )
        context.habilidad.save()

        lista_voluntarios.append(voluntario_creado)
    context.emergencia.lista = lista_voluntarios


@step('priorizo los voluntarios con mas experiencia según la habilidad "{habilidad_solicitada}"')
def step_impl(context, habilidad_solicitada):
    context.emergencia.priorizar_voluntarios()


@step('tendré una lista "{lista_voluntarios_priorizada}" priorizada')
def step_impl(context, lista_voluntarios_priorizada):
    pass
