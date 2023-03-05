from behave import *
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")

from behave import step


@step(
    'que tengo un miembro del staff médico llamado '
    '"{nombre_staff}" disponible los días '
    '"{dias_disponibles}" de '
    '"{hora_inicio}" a "{hora_fin}"')
def step_impl(context, nombre_staff, dias_disponibles, hora_inicio, hora_fin):
    pass


@step(
    'hay una actividad regular de "{actividad}" '
    'los días "{dias}" de "{hora_inicio}" '
    'a "{hora_fin}" en {lugar}')
def step_impl(context, actividad, dias, hora_inicio, hora_fin, lugar):
    pass


@step(
    'el administrador del personal médico asigna a '
    '{nombre_staff} para {actividad} los días '
    '"{dias}" en {lugar}')
def step_impl(context, nombre_staff, actividad, dias, lugar):
    pass


@step(
    "el sistema actualiza automáticamente el horario de "
    "{nombre_staff}")
def step_impl(context, nombre_staff):
    pass


@step(
    '{nombre_staff} recibe una notificación sobre su participación '
    'en la actividad regular de "{actividad}" los días "{dias}" en {lugar}')
def step_impl(context, nombre_staff, actividad, dias, lugar):
    pass
