class Emergencia:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcionEmergencia = descripcion

    def enviarNotificacion(self, voluntarios, habilidades):
        for nombre in voluntarios:
            print(f"Estimado: {nombre} se necesita de su ayuda")
            print(f"Las habilidades requeridas son: {habilidades}")

    def getHabilidadesRequeridas(self):
        return self.habilidadesRequeridas
