class Voluntario:
    def __init__(self, nombre='', apellido='', edad=0, es_asignado='0', emergencia=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tiene_actividad = es_asignado
        self.emergencia = emergencia

    def get_es_asignado(self):
        return self.tiene_actividad

    def __str__(self):
        return f'Voluntario: {self.nombre}, {self.tiene_actividad}, ||{self.emergencia}||'
