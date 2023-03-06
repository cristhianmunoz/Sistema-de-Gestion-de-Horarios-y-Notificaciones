from behave import *
from faker import Faker
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.habilidad_model import Habilidad
from gestion_voluntarios.model.voluntario_model import Voluntario

use_step_matcher("parse")

faker = Faker('es_ES')


@step('que tengo una emergencia que necesita de "{vacantes:n}" voluntarios con la habilidad "{habilidad_solicitada}"')
def step_impl(context, vacantes, habilidad_solicitada):
    context.emergencia = Emergencia(
        vacantes=int(vacantes),
        habilidad_requerida=habilidad_solicitada
    )
    context.emergencia.save()


@step('tengo a varios "{lista_voluntarios_confirmados}" que confirmaron la asistencia')
def step_impl(context, lista_voluntarios_confirmados):
    lista = eval(lista_voluntarios_confirmados)
    lista_voluntarios = []
    i = 0
    for voluntario in lista.values():
        voluntario_creado = Voluntario(
            nombre=voluntario["nombre"],
            apellido=voluntario["apellido"],
            edad=faker.random_int(min=18, max=60)
        )
        voluntario_creado.save()

        for habilidad in voluntario["habilidad"]:
            habilidad_voluntario = Habilidad(
                titulo=habilidad,
                descripcion=faker.text(max_nb_chars=200),
                horas_experiencia=float(voluntario["horas_experiencia"][i]),
                voluntario_id=voluntario_creado.id
            )
            habilidad_voluntario.save()
            i += 1
        i = 0
        lista_voluntarios.append(voluntario_creado)
    context.emergencia.lista = lista_voluntarios


@step('priorizo los voluntarios con mas experiencia según la habilidad "{habilidad_solicitada}"')
def step_impl(context, habilidad_solicitada):
    context.lista_priorizada = context.emergencia.priorizar_voluntarios()


@step('tendré una lista "{lista_voluntarios_priorizada}" priorizada')
def step_impl(context, lista_voluntarios_priorizada):
    print(context.emergencia.obtener_lista_nombres())
    assert context.emergencia.obtener_lista_nombres() == eval(lista_voluntarios_priorizada)
