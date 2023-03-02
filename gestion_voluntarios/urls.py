from django.urls import path

from .controller import voluntario_test_controller

urlpatterns = [
    path('', voluntario_test_controller.index, name='index'),
]
