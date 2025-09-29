import logging

from datetime import datetime

class Persona:

    id = 0
    personajes = []

    def __init__(self, nombre, apellidos, fecha_nacimiento, puntuacionTotal):

        Persona.id += 1
        self._nombre = nombre
        self._apellidos = apellidos
        self._fecha_nacimiento = fecha_nacimiento
        self.puntuacionTotal = puntuacionTotal

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        self._apellidos = value

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value

    def saberEdadPersonaje(self):
        fecha_hoy = datetime.now()
        anio_hoy = fecha_hoy.year
        edad = anio_hoy - self.fecha_nacimiento

        logging.info(f"La edad de {self.nombre} {self.apellidos} es de {edad} ")

        return edad


    def __str__(self):
        return f"Persona(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, " \
            f"fecha_nacimiento={self.fecha_nacimiento}, puntuacionTotal={self.puntuacionTotal})"
