from django.urls import path
from gestion_voluntarios.controller import asignar_voluntarios_controller

from .view import voluntario_view

urlpatterns = [
    path('', voluntario_view.index, name='index'),
    # path('gestion_voluntarios/controller/asignar_voluntarios_controller',
    #      asignar_voluntarios_controller.cerrar_popup_voluntarios, name='cerrar_popup_voluntarios'),
    path('gestion_voluntarios/controller/asignar_voluntarios_controller',
         asignar_voluntarios_controller.asignar_voluntarios, name='asignar_voluntarios'),
    path('gestion_voluntarios/controller/asignar_voluntarios_controller',
         asignar_voluntarios_controller.get_id_emergencia, name='get_id_emergencia'),
]
