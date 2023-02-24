from django.db import models


class DiaSemana(models.TextChoices):
    Lunes = 'Lunes'
    Martes = 'Martes'
    Miercoles = 'Miércoles'
    Jueves = 'Jueves'
    Viernes = 'Viernes'
    Sabado = 'Sábado'
    Domingo = 'Domingo'


class Habilidad(models.TextChoices):
    suturar = 'suturar'


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)

    def comprobarDisponibilidad(self):
        pass


class Horario(models.Model):
    class Meta:
        abstract = True


class HorarioVoluntario(Horario):
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)


class Dia(models.Model):
    diaSemana = models.CharField(max_length=50, choices=DiaSemana.choices, default='')
    horario = models.ForeignKey(HorarioVoluntario, on_delete=models.CASCADE)


class Periodo(models.Model):
    horaInicio = models.CharField(max_length=5, default='')
    horaFin = models.CharField(max_length=5, default='')
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)


class Habilidades(models.Model):
    nombre = models.CharField(max_length=20, choices=Habilidad.choices, default='')
    descripcion = models.CharField(max_length=50, default='')
    horasExperiencias: models.IntegerField(default=0)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
