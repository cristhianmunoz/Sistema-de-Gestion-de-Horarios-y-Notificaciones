from behave import *
from gestion_voluntarios.model.periodo_model import Periodo, DiaSemana

use_step_matcher("parse")


@step(
    'el horario de la institución médica tiene disponible los dias '
    '"{dia_disponible}" en el periodo de "{hora_inicio_disponible}" a '
    '"{hora_final_disponible}" horas para asignar una actividad')
def step_impl(context, dia_disponible, hora_inicio_disponible, hora_final_disponible):

    pass




@step(
    'el administrador del personal médico asigne el horario los dias "{dia_solicitado}" '
    'en el periodo de "{hora_inicio_solicitada}" a "{hora_final_solicitada}" '
    'horas para la actividad "{actividad_solicitada}"')
def step_impl(context, dia_solicitado, hora_inicio_solicitada, hora_final_solicitada, actividad_solicitada):
    pass


@step(
    'el sistema asignara el horario los dias "{dia_asignado}" en el periodo de "{hora_inicio_asignada}" '
    'a "{hora_final_asignada}" horas para la actividad "{actividad_asignada}"')
def step_impl(context, dia_asignado, hora_inicio_asignada, hora_final_asignada, actividad_asignada):
    pass


@step(
    'que el horario de la institución médica tiene asignado un horario los dias '
    '"{dia_asignado}" en el periodo de "{inicio_asignado}" a "{final_asignado}" '
    'horas para la actividad "{actividad_solicitada}"')
def step_impl(context, dia_asignado, inicio_asignado, final_asignado, actividad_solicitada):
    pass


@step(
    'el administrador del personal médico asigne el horario los dias "{dia_solicitado}"'
    ' en el periodo de "{inicio_solicitado}" a "{final_solicitado}" horas para '
    'la actividad "{actividad_solicitada}"')
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado, actividad_solicitada):
    pass


@step(
    'el sistema asignara el horario los dias "{dia_solicitado}" en el periodo de "{inicio_solicitado}" '
    'a "{final_solicitado}" horas para la actividad "{actividad_solicitada}" en paralelo a el horario anterior')
def step_impl(context, dia_solicitado, inicio_solicitado, final_solicitado, actividad_solicitada):
    pass