class Actividad:
    def __init__(self, nombre='', tiene_voluntario='0', emergencia=None):
        self.nombre = nombre
        self.tiene_voluntario = tiene_voluntario
        self.emergencia = emergencia
        self.voluntarios = []

    def asignar_voluntario(self, voluntario):
        self.voluntarios.append(voluntario)
        self.tiene_voluntario = '1'
        voluntario.es_asignado = '1'

    def get_tiene_voluntario(self):
        return self.tiene_voluntario

    def __str__(self):
        return f'Actividad: {self.nombre}, {self.tiene_voluntario}, ||{self.emergencia}||, ||{self.voluntarios}||'
