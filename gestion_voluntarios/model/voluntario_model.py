from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)

    # habilidades = models.ManyToManyField(Habilidad)
    # horarioDisponible = models.OneToOneField('Horario', on_delete=models.CASCADE)

    def comprobar_disponibilidad(self):
        pass

