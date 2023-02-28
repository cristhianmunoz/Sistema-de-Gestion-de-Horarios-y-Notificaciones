from behave import *
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.voluntario_model import Voluntario
from gestion_voluntarios.model.actividad_model import Actividad

use_step_matcher("parse") #Sirve para matchear .feature y este .py


@step('que se tiene una emergencia que aún no es atendida')
def step_impl(context):
    context.emergencia = Emergencia()
    pass


@step('hay un grupo de voluntarios que asistirán sin actividades asignadas')
def step_impl(context):
    context.voluntario = Voluntario()
    pass


@step('se les asigna al menos una actividad a cada voluntario')
def step_impl(context):
    context.actividad = Actividad("Suturar", context.emergencia)
    assert context.actividad.asignarVoluntario(context.voluntario)
    pass


@step('la emergencia será atendida')
def step_impl(context):
    context.emergencia.obtener_esAtendida(True)
    pass

