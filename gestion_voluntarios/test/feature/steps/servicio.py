from behave import *

from gestion_voluntarios.model.models import *


@step("que tengo una emergencia y existe un registro de voluntarios")
def step_impl(context):
    """
        :type context: behave.runner.Context
        """
    context.habilidadesRequeridas = [Habilidad("descripcionHabilidad")]
    context.emergencia = Emergencia("descripcion", context.habilidadesRequeridas)
    context.habilidades = [Habilidad("descripcionHabilidad"), Habilidad("descripcionHabilidad")]
    context.voluntarios = [Voluntario("Pepito", context.habilidades), Voluntario("Juan", context.habilidades)]
    use_step_matcher("parse")

    # raise NotImplementedError(u'STEP: Dado que tengo una emergencia y existe un registro de voluntarios')


@step("realice una petición de servicios con las habilidades requeridas para atender esa emergencia")
def step_impl(context):
    """
            :type context: behave.runner.Context
            """
    # raise NotImplementedError(u'STEP: Cuando realice una petición de servicios con las habilidades requeridas para
    # atender esa emergencia')


@step("se enviara una notificación a los voluntarios con la emergencia y la lista de habilidades requeridas")
def step_impl(context):
    """
            :type context: behave.runner.Context
            """
    # raise NotImplementedError(u'STEP: Entonces se enviará una notificación a los voluntarios con la emergencia y la
    # lista de habilidades requeridas')
