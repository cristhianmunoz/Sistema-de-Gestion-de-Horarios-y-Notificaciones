import django
from django.db import models
from django.db import connection

from gestion_voluntarios.model.emergencia_model import Emergencia

django.setup()


class Actividad(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default='')
    tiene_voluntario = models.BooleanField(default=False)
    emergencia = models.ForeignKey(Emergencia,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True,
                                   related_name='actividades'
                                   )
    # Revisar esta relación (una actividad muchos voluntarios - un voluntario muchas actividades)
    voluntarios = models.ManyToManyField('Voluntario')

    def asignar_voluntario(self, voluntario):
        self.voluntarios.add(voluntario)
        self.tiene_voluntario = True
        voluntario.es_asignado = True
        voluntario.save()
        self.save()

    def get_tiene_voluntario(self):
        return self.tiene_voluntario

    def get_voluntarios(self):
        return self.voluntarios.all()
