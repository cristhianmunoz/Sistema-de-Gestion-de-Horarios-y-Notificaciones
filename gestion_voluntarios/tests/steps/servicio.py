from behave import *

from gestion_voluntarios.model.emergencia_model import Emergencia

use_step_matcher("parse")


@step('que tengo una emergencia con titulo "{tituloEmergencia}" y su descripción "{descripcionEmergencia}"')
def step_impl(context, tituloEmergencia, descripcionEmergencia):
    context.emergencia = Emergencia(tituloEmergencia, descripcionEmergencia)


@step(
    'necesito "{numeroDeVoluntariosRequeridos}" voluntarios para atender la emergencia con las siguientes habilidades '
    'requeridas: "{habilidadesRequeridas}"')
def step_impl(context, numeroDeVoluntariosRequeridos, habilidadesRequeridas):
    context.numeroDeVoluntariosRequeridos = numeroDeVoluntariosRequeridos
    context.habilidadesRequeridas = habilidadesRequeridas.split(",")


@step('solicite servicios a los "{voluntarios}" registrados en el sistema')
def step_impl(context, voluntarios):
    pass


@step('las "{habilidadesVoluntarios}" coincidan con las "{habilidadesRequeridas}"')
def step_impl(context, habilidadesVoluntarios, habilidadesRequeridas):
    pass


@step('el "{numeroDeVoluntariosRequeridos}" sea igual a la cantidad de "{voluntariosSeleccionados}"')
def step_impl(context, numeroDeVoluntariosRequeridos, voluntariosSeleccionados):
    pass


@step('se enviara "{numeroDeNotificaciones}" en base a los "{voluntariosSeleccionados}"')
def step_impl(context, numeroDeNotificaciones, voluntariosSeleccionados):
    pass
