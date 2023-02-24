class Habilidad():
    def __init__(self, descripcionHabilidad):
        self.descripcionHabilidad = descripcionHabilidad


class Emergencia:
    def __init__(self, descripcion, habilidades):
        self.descripcion = descripcion
        self.habilidades = habilidades


class Voluntario:
    def __init__(self, nombre, habilidades):
        self.nombre = nombre
        self.habilidades = habilidades
