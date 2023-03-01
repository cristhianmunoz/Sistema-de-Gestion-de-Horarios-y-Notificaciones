class Actividad:
    def __init__(self, nombre='', es_asignada='0', emergencia=None, voluntarios=None):
        self.nombre = nombre
        self.es_asignada = es_asignada
        self.emergencia = emergencia
        self.voluntarios = voluntarios or []

    def asignar_actividad(self, voluntario):
        self.es_asignada = '1'
        voluntario.tiene_actividad = '1'
        self.voluntarios.append(voluntario)

    def get_es_asignada(self):
        return self.es_asignada
