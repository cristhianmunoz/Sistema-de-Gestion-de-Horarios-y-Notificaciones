import datetime
import os

import django

from behave import *
from behave import step
from faker.generator import random

from gestion_voluntarios.model.actividad_model import Actividad
from gestion_voluntarios.model.dia_semana_model import DiaSemana
from gestion_voluntarios.model.emergencia_model import Emergencia
from gestion_voluntarios.model.horario_model import Horario
from gestion_voluntarios.model.periodo_model import Periodo
from gestion_voluntarios.model.voluntario_model import Voluntario
from faker import Faker

use_step_matcher("parse")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notificaciones_medicas.settings')

faker = Faker("es_ES")

django.setup()

@step('que existe una emergencia registrada en el sistema con el nombre "{nombre}"')
def step_impl(context, nombre):
    nombre_emergencia = faker.name()
    context.emergencia = Emergencia(nombre=nombre_emergencia)
    context.emergencia.save()


@step('que tengo un grupo de "{cantidad_voluntarios}" voluntarios con sus horarios de disponibilidad')
def step_impl(context, cantidad_voluntarios):

    cantidad_voluntarios_int = int(cantidad_voluntarios)
    context.cantidad_voluntarios = cantidad_voluntarios_int

    for i in range(cantidad_voluntarios_int):
        # Creación del voluntario
        context.voluntario= Voluntario(nombre=faker.first_name(),
                                            apellido=faker.last_name(),
                                            edad=faker.random_int(min=18, max=80),
                                            emergencia=context.emergencia)
        context.voluntario.save()

        # Creación del horario del voluntario
        context.horario = Horario(
            voluntario_id=context.voluntario.id
        )

        context.horario.save()

        # Periodo de disponibilidad del voluntario
        dia_semana_test = random.choice(list(DiaSemana))
        hora_inicio_test = datetime.time(random.randint(9, 12))
        hora_fin_test = datetime.time(random.randint(14, 18))

        context.periodo = Periodo(
            dia_semana=dia_semana_test,
            hora_inicio=hora_inicio_test,
            hora_fin=hora_fin_test,
            horario_id=context.horario.id
        )
        context.periodo.save()

        time1 = context.periodo.hora_inicio.strftime("%H:%M:%S")
        time2 = context.periodo.hora_fin.strftime("%H:%M:%S")

        print("Voluntario:" + context.periodo.dia_semana + "  " + time1 + " -> " + time2)

        context.emergencia.add_voluntarios(context.voluntario)


@step('la emergencia tiene registradas "{cantidad_actividades}" actividades con horarios definidos')
def step_impl(context, cantidad_actividades):

    cantidad_actividades_int = int(cantidad_actividades)
    context.cantidad_actividades = cantidad_actividades_int

    for i in range(cantidad_actividades_int):
        context.actividad = Actividad(nombre=faker.name(),
                                        emergencia=context.emergencia)

        context.actividad.save()

        context.horarioAct = Horario(
            actividad_id=context.actividad.id
        )

        context.horarioAct.save()

        # Periodo de la actividad
        dia_semana_test = random.choice(list(DiaSemana))
        hora_inicio_test = datetime.time(random.randint(9, 12))
        hora_fin_test = datetime.time(random.randint(14, 18))

        context.periodoAct = Periodo(
            dia_semana=dia_semana_test,
            hora_inicio=hora_inicio_test,
            hora_fin=hora_fin_test,
            horario_id=context.horario.id
        )

        context.periodoAct.save()
        time1 = context.periodoAct.hora_inicio.strftime("%H:%M:%S")
        time2 = context.periodoAct.hora_fin.strftime("%H:%M:%S")

        print("Actividad:" + context.periodoAct.dia_semana + "  " + time1 + " -> " + time2)

        context.emergencia.add_actividades(context.actividad)


@step("al comparar los horarios de disponibilidad de cada voluntario con los horarios de cada actividad")
def step_impl(context):
    lista_actividades = context.emergencia.get_actividades()
    lista_voluntarios = context.emergencia.get_voluntarios()
    actividades_sin_match = context.actividad.obtenerActividadesCriticas(lista_actividades, lista_voluntarios)

    context.actividades_sin_match = actividades_sin_match

@step(
    "debería poder identificar los períodos en los que no hay ningún voluntario disponible para cada actividad de la emergencia")
def step_impl(context):
    periodos_criticos = []

    for actividad in context.actividades_sin_match:
        periodo = actividad.get_periodos()
        periodos_criticos.append(periodo)

    context.periodos_criticos = periodos_criticos


@step('debería poder visualizar los tiempos críticos de la emergencia "Emergencia X" de manera clara y detallada')
def step_impl(context):
    if context.actividades_sin_match:
        print('TIEMPOS CRÍTICOS:')
        for actividad in context.actividades_sin_match:
            info = actividad.get_actividad_str()
            print("Emergencia:" + info.emergencia)
            print("Actividad:" + info.nombre)
            print("Periodos:" + info.periodos + '\n\n')
    else:
        print('No existen tiempos críticos.')
