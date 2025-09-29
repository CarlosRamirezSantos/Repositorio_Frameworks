from clases.persona import Persona

class Villano(Persona):

    def __init__(self, nombre, apellidos, fecha_nacimiento, puntuacionTotal, chagepeteador, entregadorTardio, ausencias, hablador):
        super(Villano, self).__init__(nombre, apellidos, fecha_nacimiento, puntuacionTotal)
        Persona.id += 1
        self.chagepeteador = chagepeteador
        self.entregadorTardio = entregadorTardio
        self.ausencias = ausencias
        self.hablador = hablador


    def __str__(self):
        return (f"Villano(nombre={self.nombre}, apellidos={self.apellidos}, "
                f"fecha_nacimiento={self.fecha_nacimiento}, puntuacionTotal={self.puntuacionTotal}, "
                f"chagepeteador={self.chagepeteador}, entregadorTardio={self.entregadorTardio}, "
                f"ausencias={self.ausencias}, hablador={self.hablador})")

