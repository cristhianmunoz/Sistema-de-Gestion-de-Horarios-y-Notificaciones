# from datetime import datetime
from django.db import models


class Emergencia:
    def __init__(self, asunto, tipo_emergencia, ubicacion, hora_entrada, encargado, dirigido_a, actividades, detalle, respuesta):
        self.asunto = asunto
        self.tipo_emergencia = tipo_emergencia
        self.ubicacion = ubicacion
        self.hora_entrada = hora_entrada
        self.encargado = encargado
        self.dirigido_a = dirigido_a
        self.actividades = actividades
        self.detalle = detalle
        self.respuesta = respuesta

    asunto = models.CharField(max_length=200, default='')
    tipo_emergencia = models.CharField(max_length=20, default='')
    ubicacion = models.CharField(max_length=300, default='')
    hora_entrada = models.CharField(max_length=20, default='')
    encargado = models.CharField(max_length=20, default='')
    dirigido_a = models.CharField(max_length=200, default='')
    # debería ser un arreglo de voluntarios
    actividades = models.CharField(max_length=200, default='')
    detalle = models.CharField(max_length=500, default='')
    respuesta = models.BooleanField(default=False)

    def notificar(self):
        texto = F'{self.asunto} \nEstimado {self.dirigido_a} el doctor {self.encargado} solicita su presencia en ' \
                F'{self.ubicacion} a las {self.hora_entrada} para atender un(a) {self.tipo_emergencia} ' \
                F'\nLas actividades a realizar son: \n {self.actividades} ' \
                F'\nConsideraciones a tener en cuenta: \n {self.detalle}'
        return texto
