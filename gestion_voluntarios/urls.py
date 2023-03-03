from django.urls import path
from gestion_voluntarios.views import  index

from .view import voluntario_view

urlpatterns = [
    path('', voluntario_view.index, name='index'),
]
