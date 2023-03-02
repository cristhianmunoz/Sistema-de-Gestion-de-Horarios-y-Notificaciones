from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)

    def comprobar_disponibilidad(self):
        pass

    @classmethod
    def obtener_voluntario_por_id(cls, id_voluntario):
        pass
