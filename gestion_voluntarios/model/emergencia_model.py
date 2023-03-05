import django
from django.db import models

django.setup()


class Emergencia(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default='')
    nombre = models.CharField(max_length=50, default='')
    es_atendida = models.BooleanField(default=False)

    def verificar_emergencia(self):
        # Comprobar que todos tengan True
        if self.verificar_voluntarios() and self.verificar_actividades():
            # Se cambia el valor de la bandera
            self.es_atendida = True
            self.save()

    def verificar_actividades(self):
        # Recorrer actividades y verificar su valor en tiene_voluntario
        respuesta = False
        actividades = self.actividades.all()
        for actividad in actividades:
            if actividad.get_tiene_voluntario():
                respuesta = True
            else:
                respuesta = False
        return respuesta

    def verificar_voluntarios(self):
        # Recorrer voluntarios y verificar su valor en es_asignado
        respuesta = False
        voluntarios = self.voluntarios.all()
        for voluntario in voluntarios:
            if voluntario.get_es_asignado():
                respuesta = True
            else:
                respuesta = False
        return respuesta


    def add_actividades(self, actividad):
        self.actividades.add(actividad)

    def add_voluntarios(self, voluntario):
        self.voluntarios.add(voluntario)

    def get_es_atendida(self):
        return self.es_atendida

    def get_id(self):
        return self.id

    def get_voluntarios(self):
        return self.voluntarios.all()

    def __str__(self):
        return f'Emergencia: {self.nombre}, {self.es_atendida}, ||{self.voluntarios.all()}||, ' \
               f'||{self.actividades.all()}||'
