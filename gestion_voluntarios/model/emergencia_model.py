class Emergencia:
    def __init__(self, nombre='', es_atendida='0'):
        self.nombre = nombre
        self.es_atendida = es_atendida
        self.voluntarios = []
        self.actividades = []

    def verificar_emergencia(self):
        # comprobar que todos tengan 1
        # Se cambia el valor de la bandera
        self.es_atendida = '1'

    def add_actividades(self, actividad):
        self.actividades.append(actividad)

    def add_voluntarios(self, voluntario):
        self.voluntarios.append(voluntario)

    def get_es_atendida(self):
        return self.es_atendida

    def __str__(self):
        return f'Emergencia: {self.nombre}, {self.es_atendida}, ||{self.voluntarios}||, ||{self.actividades}||'
