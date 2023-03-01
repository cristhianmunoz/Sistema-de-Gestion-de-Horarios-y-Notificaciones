class Actividad:
    def __init__(self, nombre='', tiene_voluntario='0', emergencia=None, voluntarios=None):
        self.nombre = nombre
        self.es_asignada = tiene_voluntario
        self.emergencia = emergencia
        self.voluntarios = voluntarios or []

    def asignar_voluntario(self, voluntario):
        self.voluntarios.append(voluntario)
        self.es_asignada = '1'
        voluntario.tiene_actividad = '1'

    def get_tiene_voluntario(self):
        return self.es_asignada

    def __str__(self):
        return f'({self.nombre}, {self.es_asignada}, {self.emergencia}, {self.voluntarios})'
