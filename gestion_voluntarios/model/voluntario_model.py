from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)
    habilidades = models.CharField(max_length=500, default='')
    estado = models.BooleanField(default=False)

    # habilidades = models.ManyToManyField(Habilidad)
    # horarioDisponible = models.OneToOneField('Horario', on_delete=models.CASCADE)

    def comprobar_disponibilidad(self):
        pass

    def respuesta(self, emergencia_aceptada):
        if not emergencia_aceptada:
            bool_respuesta = 'Se ha rechazado la solicitud enviada'
            return bool_respuesta
        else:
            bool_respuesta = 'Se ha confirmado la solicitud enviada'
            return bool_respuesta