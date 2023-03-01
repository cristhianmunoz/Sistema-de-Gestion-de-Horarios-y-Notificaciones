from django.db import models

class Emergencia(models.Model):
    nombre = models.CharField(max_length=50, default='')
    # Estado que define si la emergencia fue o no atendida
    esAtendida = models.BooleanField(default=False)



    def verificarEmergencia(self):
        self.esAtendida = True


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)
    # Estado que define si tiene o no una actividad asignada
    tieneActividad = models.BooleanField(default=False)


    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE)


class Actividad(models.Model):
    nombre = models.CharField(choices=ActividadEmergencia.choices)
    esAsignada = models.BooleanField(default=False)

    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE)
    voluntarios = models.ManyToManyField(Voluntario)

    def asignarActividad(self, voluntario, actividad):
        actividad.esAsignada = True
        voluntario.tieneActividad = True

class ActividadEmergencia(models.TexChoices):
    EVACUAR = 'Evacuar'
    PRIMEROS_AUXILIOS = 'Primeros auxilios'