from clases.persona import Persona

class Heroe(Persona):

    def __init__(self, nombre, apellidos, fecha_nacimiento, puntuacionTotal, codigoLimpio, bienDocumentado, gitGod, arquitecto, detallista):
        super(Heroe, self).__init__(nombre, apellidos, fecha_nacimiento, puntuacionTotal)
        Persona.id += 1
        self.codigoLimpio = codigoLimpio
        self.bienDocumentado = bienDocumentado
        self.gitGod = gitGod
        self.arquitecto = arquitecto
        self.detallista = detallista

    def __str__(self):
        return (f"Heroe(nombre={self.nombre}, apellidos={self.apellidos}, "
                f"fecha_nacimiento={self.fecha_nacimiento}, puntuacionTotal={self.puntuacionTotal}, "
                f"codigoLimpio={self.codigoLimpio}, bienDocumentado={self.bienDocumentado}, "
                f"gitGod={self.gitGod}, arquitecto={self.arquitecto}, detallista={self.detallista})")