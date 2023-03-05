from django.urls import path

from .controller import voluntario_home_controller

urlpatterns = [
    path('', voluntario_home_controller.index, name='index'),
]
