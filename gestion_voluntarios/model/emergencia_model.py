import django

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica

django.setup()
from django.db import models


class Emergencia(models.Model):
    vacantes = models.IntegerField(default=0)
    habilidad_requerida = models.CharField(choices=HabilidadMedica.choices)

    def __int__(self, vacantes, habilidad_requerida):
        self.vacantes = vacantes
        self.habilidad_requerida = habilidad_requerida
        self.lista_priorizada = []
        self.lista = []

    def priorizar_voluntarios(self, habilidad_requerida):
        voluntarios = self.obtener_horas_experiencia(habilidad_requerida)
        #self.lista_priorizada = sorted(voluntarios, key=lambda x: x['horas_experiencia'], reverse=True)

    def agregar_voluntarios(self, lista_voluntarios_confirmados):
        # assert isinstance(lista_voluntarios_confirmados, object)
        self.lista = lista_voluntarios_confirmados

    def obtener_horas_experiencia(self, habilidad_solicitada):
        voluntarios_habilidad = self.obtener_voluntarios_habilidad(habilidad_solicitada)
        voluntarios = []
        for voluntario in voluntarios_habilidad:
            voluntarios.append({"voluntario": voluntario,
                                "habilidad_voluntario": voluntario.obtenerHabilidades(),
                                "horas_experiencia": voluntario.habilidades.obtenerHoras()})
        return voluntarios

    def obtener_voluntarios_habilidad(self, habilidad_solicitada):
        for voluntario in self.lista:
            print("Este voluntario: " + voluntario.nombre)

    def obtener_lista_priorizada(self):
        return self.lista_priorizada
