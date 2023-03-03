import django
from django.db import models
from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica

django.setup()


class Emergencia(models.Model):
    id = models.AutoField(primary_key=True)
    vacantes = models.IntegerField(default=0)
    habilidad_requerida = models.TextField(choices=HabilidadMedica.choices)
    lista_priorizada = []

    def priorizar_voluntarios(self):
        lista_ordenada = sorted(self.lista, key=lambda x: x.horas_experiencia_habilidad(self.habilidad_requerida) or 0, reverse=True)
        print("Lista ordenada")
        for voluntario in lista_ordenada:
            print(voluntario.nombre + " " + str(voluntario.horas_experiencia_habilidad(self.habilidad_requerida)))