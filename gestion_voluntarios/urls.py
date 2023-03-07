from django.urls import path

from gestion_voluntarios.controller import voluntario_home_controller
from gestion_voluntarios.controller import voluntario_habilidad_controller
from gestion_voluntarios.controller import voluntario_horario_controller

urlpatterns = [
    path('voluntario', voluntario_home_controller.index, name='voluntario'),
    path('habilidad', voluntario_habilidad_controller.index, name='habilidad'),
    path('horario', voluntario_horario_controller.index, name='horario'),
]
