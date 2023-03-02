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

    def __str__(self):
        return f'Emergencia: {self.nombre}, {self.es_atendida}, ||{self.voluntarios.all()}||, ' \
               f'||{self.actividades.all()}||'


# class ActividadEmergencia(models.TexChoices):
#    EVACUAR = 'Evacuar'
#    PRIMEROS_AUXILIOS = 'Primeros auxilios'


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

    def get_tiene_voluntario(self):
        return self.tiene_voluntario

    def __str__(self):
        return f'Actividad: {self.nombre}, {self.tiene_voluntario}, ||{self.voluntarios.all()}||'


class Voluntario(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default='')
    nombre = models.CharField(max_length=50, default='')
    es_asignado = models.BooleanField(default=False)
    emergencia = models.ForeignKey(Emergencia, on_delete=models.CASCADE, related_name='voluntarios')

    def get_es_asignado(self):
        return self.es_asignado

    def __str__(self):
        return f'Voluntario: {self.nombre}, {self.es_asignado}'
