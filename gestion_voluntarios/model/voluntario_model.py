class Voluntario:
    def __init__(self, nombre='', apellido='', edad=0, tiene_actividad='0', emergencia=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tiene_actividad = tiene_actividad
        self.emergencia = emergencia


    def get_tiene_actividad(self):
        return self.tiene_actividad
