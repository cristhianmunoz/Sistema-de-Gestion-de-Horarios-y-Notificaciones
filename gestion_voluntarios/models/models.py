# from datetime import datetime
# from django.db import models


class Voluntario:
    def __init__(self, nombre, apellido, edad, habilidades):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.habilidades = habilidades

    def respuesta(self, emergencia_aceptada):
        if not emergencia_aceptada:
            string_respuesta = 'Se ha rechazado la solicitud enviada'
            return string_respuesta
        else:
            string_respuesta = 'Se ha confirmado la solicitud enviada'
            return string_respuesta


class Emergencia:
    def __init__(self, asunto, ubicacion, tipo_emergencia, hora_entrada, encargado, actividades, detalle, dirigido_a):
        self.asunto = asunto
        self.tipo_emergencia = tipo_emergencia
        self.ubicacion = ubicacion
        self.hora_entrada = hora_entrada
        self.encargado = encargado
        self.dirigido_a = dirigido_a
        self.actividades = actividades
        self.detalle = detalle

    def notificar(self):
        texto = F'{self.asunto} \nEstimado {self.dirigido_a} el doctor {self.encargado} solicita su presencia en ' \
                F'{self.ubicacion} a las {self.hora_entrada} para atender un(a) {self.tipo_emergencia} ' \
                F'\nLas actividades a realizar son: \n {self.actividades} ' \
                F'\nConsideraciones a tener en cuenta: \n {self.detalle}'
        return texto
