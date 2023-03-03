from django.urls import path

from .view import voluntario_view

urlpatterns = [
    path('', voluntario_view.index, name='index'),
]
