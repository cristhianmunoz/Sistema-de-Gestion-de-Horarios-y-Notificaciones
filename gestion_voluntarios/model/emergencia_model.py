import django
from django.db import models
from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica

django.setup()


class Emergencia(models.Model):
    id = models.AutoField(primary_key=True)
    vacantes = models.IntegerField(default=0)
    habilidad_requerida = models.TextField(choices=HabilidadMedica.choices)
    lista_priorizada = []
    lista = []

    def priorizar_voluntarios(self):
        lista_ordenada = [voluntario.horas_experiencia_habilidad(self.habilidad_requerida)for voluntario in self.lista]
        voluntarios_con_habilidad = list(filter(lambda x: x.titulo == self.habilidad_requerida, lista_ordenada))
        voluntarios_sin_habilidad = list(filter(lambda x: x.titulo != self.habilidad_requerida, lista_ordenada))
        self.lista_priorizada = self.ordenar_voluntarios(voluntarios_con_habilidad) + self.ordenar_voluntarios(
            voluntarios_sin_habilidad)[:self.vacantes]
        return self.lista_priorizada

    def ordenar_voluntarios(self, lista_filter):
        return sorted(lista_filter, key=lambda x: x.horas_experiencia, reverse=True)

    def obtener_lista_nombres(self):
        lista_voluntarios = [habilidad.voluntario for habilidad in self.lista_priorizada]
        return [voluntario.nombre + " " + voluntario.apellido for voluntario in lista_voluntarios]