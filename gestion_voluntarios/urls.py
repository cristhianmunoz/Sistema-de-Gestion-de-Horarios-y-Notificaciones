from django.urls import path

from gestion_voluntarios.controller import voluntario_home_controller
from gestion_voluntarios.controller import voluntario_habilidad_controller
from gestion_voluntarios.controller import voluntario_horario_controller
from gestion_voluntarios.controller import asignar_voluntarios_controller
from gestion_voluntarios.controller import priorizar_voluntario_controller

urlpatterns = [
    # path('', voluntario_view.index, name='index'),
    path('voluntario', voluntario_home_controller.index, name='voluntario'),
    path('habilidad', voluntario_habilidad_controller.index, name='habilidad'),
    path('horario', voluntario_horario_controller.index, name='horario'),
    path('actividad', asignar_voluntarios_controller.index, name='actividad'),
    path('asignar', asignar_voluntarios_controller.asignar_voluntarios, name='asignar_voluntarios'),
    path('priorizar', priorizar_voluntario_controller.index, name='index'),
]
