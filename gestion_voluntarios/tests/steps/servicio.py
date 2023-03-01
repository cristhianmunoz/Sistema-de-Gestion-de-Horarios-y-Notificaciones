from behave import *

from gestion_voluntarios.model.emergencia_model import Emergencia

use_step_matcher("re")


@step(
    'que tengo una emergencia con titulo "(?P<tituloEmergencia>.+)" y su descripción "(?P<descripcionEmergencia>.+)" '
    'y necesito "(?P<habilidadesRequeridas>.+)"')
def step_impl(context, tituloEmergencia, descripcionEmergencia, habilidadesRequeridas):
    context.emergencia = Emergencia(tituloEmergencia, descripcionEmergencia, habilidadesRequeridas)
    raise NotImplementedError(
        u'STEP: Dado que tengo una emergencia con titulo "<tituloEmergencia>" y su descripción '
        u'"<descripcionEmergencia>" y necesito "<habilidadesRequeridas>"')


@step(
    'realice una petición de servicios con las "(?P<habilidadesRequeridas>.+)" para atender esa emergencia a los '
    '"(?P<voluntarios>.+)"')
def step_impl(context, habilidadesRequeridas, voluntarios):
    context.solicitarServicios(habilidadesRequeridas)
    raise NotImplementedError(
        u'STEP: Cuando realice una petición de servicios con las "<habilidadesRequeridas>" para atender esa '
        u'emergencia a los "<voluntarios>"')


@step(
    'se enviara una notificacion a los "(?P<voluntarios>.+)" con la emergencia y la lista de "(?P<habilidadesRequeridas>.+)"')
def step_impl(context, voluntarios, habilidadesRequeridas):
    context.enviarNotificacion(voluntarios, habilidadesRequeridas)
    raise NotImplementedError(
        u'STEP: Entonces se enviara una notificacion a los "<voluntarios>" con la emergencia y la lista de "<habilidadesRequeridas>"')
