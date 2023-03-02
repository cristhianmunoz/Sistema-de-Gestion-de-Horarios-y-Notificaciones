from behave import *

from gestion_voluntarios.model.emergencia_model import Emergencia

use_step_matcher("parse")


@step(
    'que tengo una emergencia con titulo "{tituloEmergencia}" y su descripción "{descripcionEmergencia}" '
    'y necesito "{habilidadesRequeridas}')
def step_impl(context, tituloEmergencia, descripcionEmergencia, habilidadesRequeridas):
    context.habilidadesRequeridas = habilidadesRequeridas.split(",")
    context.emergencia = Emergencia(tituloEmergencia, descripcionEmergencia, context.habilidadesRequeridas)


@step(
    'solicite servicios a los "{voluntarios}" registrados en el sistema'
)
def step_impl(context, voluntarios):
    context.voluntarios = voluntarios.split(",")



@step(
    'se enviara una notificacion a los voluntarios con la lista de habilidades requeridas')
def step_impl(context):
    context.emergencia.enviarNotificacion(context.voluntarios, context.habilidadesRequeridas)
