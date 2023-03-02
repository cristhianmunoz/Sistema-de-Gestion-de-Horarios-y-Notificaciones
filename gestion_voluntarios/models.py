from django.db import models


class Emergencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default='')
    es_atendida = models.CharField(max_length=1, default='0')
    voluntarios = models.ManyToManyField('Voluntario')
    actividades = models.ManyToManyField('Actividad')

    def verificar_emergencia(self):
        # Comprobar que todos tengan 1
        # Se cambia el valor de la bandera
        self.es_atendida = '1'

    def add_actividades(self, actividad):
        self.actividades.add(actividad)

    def add_voluntarios(self, voluntario):
        self.voluntarios.add(voluntario)

    def get_es_atendida(self):
        return self.es_atendida

    def __str__(self):
        return f'Emergencia: {self.nombre}, {self.es_atendida}, ||{self.voluntarios.all()}||, ||{self.actividades.all()}||'


# class ActividadEmergencia(models.TexChoices):
#    EVACUAR = 'Evacuar'
#    PRIMEROS_AUXILIOS = 'Primeros auxilios'


class Actividad(models.Model):
    # nombre = models.CharField(choices=ActividadEmergencia.choices, max_length=50)
    nombre = models.CharField(max_length=50, default='')
    tiene_voluntario = models.CharField(max_length=1, default='0')
    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE)
    # Revisar esta relación (una actividad muchos voluntarios - un voluntario muchas actividades)
    voluntarios = models.ManyToManyField('Voluntario')

    def asignar_voluntario(self, voluntario):
        self.voluntarios.add(voluntario)
        self.tiene_voluntario = '1'
        voluntario.es_asignado = '1'

    def get_tiene_voluntario(self):
        return self.tiene_voluntario

    def __str__(self):
        return f'Actividad: {self.nombre}, {self.tiene_voluntario}, ||{self.emergencia}||, ||{self.voluntarios.all()}||'


class Voluntario(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    edad = models.IntegerField(default=0)
    es_asignado = models.CharField(max_length=1, default='0')
    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE)

    def get_es_asignado(self):
        return self.es_asignado

    def __str__(self):
        return f'Voluntario: {self.nombre}, {self.apellido}, {self.edad}, {self.es_asignado}, ||{self.emergencia}||'
