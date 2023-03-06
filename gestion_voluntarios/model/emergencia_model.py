# from datetime import datetime
from django.db import models


class Emergencia:
    def __init__(self,vacantes, asunto, tipo_emergencia,habilidades, ubicacion, hora_entrada, encargado, dirigido_a, actividades, detalle, respuesta):
        self.numero_de_voluntarios_requeridos=vacantes
        self.asunto = asunto
        self.tipo_emergencia = tipo_emergencia
        self.ubicacion = ubicacion
        self.hora_entrada = hora_entrada
        self.encargado = encargado
        self.dirigido_a = dirigido_a
        self.actividades = actividades
        self.detalle = detalle
        self.respuesta = respuesta
        self.habilidades_requeridas =habilidades

    asunto = models.CharField(max_length=200, default='')
    tipo_emergencia = models.CharField(max_length=20, default='')
    ubicacion = models.CharField(max_length=300, default='')
    hora_entrada = models.CharField(max_length=20, default='')
    encargado = models.CharField(max_length=20, default='')
    dirigido_a = models.CharField(max_length=200, default='')
    # debería ser un arreglo de voluntarios
    actividades = models.CharField(max_length=200, default='')
    detalle = models.CharField(max_length=500, default='')

    def notificar(self):
        texto = F'{self.asunto} \nEstimado {self.dirigido_a} el doctor {self.encargado} solicita su presencia en ' \
                F'{self.ubicacion} a las {self.hora_entrada} para atender un(a) {self.tipo_emergencia} ' \
                F'\nLas actividades a realizar son: \n {self.actividades} ' \
                F'\nConsideraciones a tener en cuenta: \n {self.detalle}'
        return texto

    def enviarNotificacion(self, voluntariosSeleccionados, habilidades):
        notificacion = 0
        for nombre in voluntariosSeleccionados:
            notificacion += 1
            print(f"Estimado: {nombre} se necesita de su ayuda")
            print(f"Las habilidades requeridas son: {habilidades}")
        return f"Se han enviado: {notificacion} notificaciones a los voluntarios seleccionados"

    def getHabilidadesRequeridas(self):
        return self.habilidades_requeridas

    @staticmethod
    def obtenerVoluntarios():
        return ['Juan', 'Carlos', 'Andres']

    def filtrarVoluntarios(self, voluntarios, habilidadesVoluntario):
        return self.obtenerVoluntarios()
        '''voluntariosSeleccionados = []
        for vol in voluntarios:
            if vol.habilidades == habilidadesVoluntario:
                voluntariosSeleccionados.append(vol)
            return voluntariosSeleccionados'''

    def obtenerNumeroVoluntariosSeleccionados(self, voluntariosSeleccionados):
        return len(voluntariosSeleccionados)

    def crear_habilidades_requeridas_emergencia(self):
        # Se crean las habilidades requeridas
        habilidades_requeridas = []
        for habilidad in habilidades:
            habilidad_descripcion = habilidad.obtener_descripcion_habilidad()
            habilidades_requeridas.append(habilidad_descripcion)
        # Lista o un array de habilidades
        return habilidades_requeridas

