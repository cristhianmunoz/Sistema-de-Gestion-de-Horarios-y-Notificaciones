import django
from django.db import models
from django.db import connection

from gestion_voluntarios.model.emergencia_model import Emergencia

django.setup()


class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default='')
    tiene_voluntario = models.BooleanField(default=False)
    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE, related_name='actividades')
    # Revisar esta relación (una actividad muchos voluntarios - un voluntario muchas actividades)
    voluntarios = models.ManyToManyField('Voluntario')

    def asignar_voluntario(self, voluntario):
        self.voluntarios.add(voluntario)
        self.tiene_voluntario = True
        voluntario.es_asignado = True
        voluntario.save()
        self.save()

    def borrar_actividad(self):
        with connection.cursor() as cursor:
            cursor.execute("delete from gestion_voluntarios_actividad where tiene_voluntario=1")


    def get_tiene_voluntario(self):
        return self.tiene_voluntario

    def __str__(self):
        return f'Actividad: {self.nombre}, {self.tiene_voluntario}, ||{self.voluntarios.all()}||'
