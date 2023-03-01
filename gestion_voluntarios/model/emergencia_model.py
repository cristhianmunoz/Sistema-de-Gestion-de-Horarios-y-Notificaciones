class Emergencia:
    def __init__(self, nombre='', es_atendida='0', voluntarios=None, actividades=None):
        self.nombre = nombre
        self.es_atendida = es_atendida
        self.voluntarios = voluntarios or []
        self.actividades = actividades or []

    def verificar_emergencia(self):
        #comprobar que todos tengan 1
        self.es_atendida = '1'

    def add_Actividades(self, actividad):
        self.voluntarios.append(actividad)

    def remove_Actividades(self, actividad):
        self.voluntarios.remove(actividad)

    def get_es_atendida(self):
        return self.es_atendida


