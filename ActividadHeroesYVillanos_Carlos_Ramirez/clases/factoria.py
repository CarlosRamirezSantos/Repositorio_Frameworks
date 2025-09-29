import random
import statistics
import logging

from clases.villano import Villano
from clases.heroe import Heroe
from clases.apellidos import ApellidosPersonajes
from clases.nombresPersonajes import NombresPersonajes


class PersonaFactoria:


    @staticmethod
    def crearHeroe():

        nombre = random.choice(list(NombresPersonajes)).value
        apellidos = random.choice(list(ApellidosPersonajes)).value
        fecha_nacimiento = random.randint(1500,2025)
        codigoLimpio = random.randint(0,100)
        bienDocumentado = random.randint(0,100)
        gitGod = random.randint(0,100)
        arquitecto = random.randint(0,100)
        detallista = random.randint(0,100)

        puntuaciones = [codigoLimpio, bienDocumentado, gitGod, arquitecto, detallista]
        puntuacionTotal = statistics.mean(puntuaciones)

        logging.info(f"Se ha creado con éxito al heroe {nombre} {apellidos}.")

        return Heroe(nombre,apellidos,fecha_nacimiento,puntuacionTotal,
                     codigoLimpio, bienDocumentado, gitGod, arquitecto,
                     detallista)


    @staticmethod
    def crearVillano():

        nombre = random.choice(list(NombresPersonajes)).value
        apellidos = random.choice(list(ApellidosPersonajes)).value
        fecha_nacimiento = random.randint(1500,2025)
        chagepeteador = random.randint(0,100)
        entregadorTardio = random.randint(0,100)
        ausencias = random.randint(0,100)
        hablador = random.randint(0,100)


        puntuaciones = [chagepeteador, entregadorTardio, ausencias, hablador]
        puntuacionTotal = statistics.mean(puntuaciones)

        logging.info(f"Se ha creado con éxito al villano {nombre} {apellidos}.")

        return Villano(nombre,apellidos,fecha_nacimiento,puntuacionTotal,
                        chagepeteador, entregadorTardio, ausencias, hablador)


    @staticmethod
    def getPersonajeByAtributo(lista_personajes, atributo, valor_buscado):

        resultados = []

        # Me faltaria aplicar el lower y el strip. Busqué como hacerlo pero me resultó un poco lioso para aplicárselo

        if lista_personajes:
            try:
                valor_convertido = int(valor_buscado)
            except ValueError:
                valor_convertido = valor_buscado

            for personaje in lista_personajes:
                if hasattr(personaje, atributo) and getattr(personaje, atributo) == valor_convertido:
                    resultados.append(personaje)
        else:

            logging.warning("La lista esta vacía")


        if not resultados:

           logging.info(f"Con {valor_buscado} no hay nadie")
        else:

            logging.info("Los personajes encontrados son: " + ", ".join(str(p) for p in resultados))

        return resultados

    @staticmethod
    def enfrentarse(heroe, villano):


        pelea = abs(heroe.puntuacionTotal - villano.puntuacionTotal)

        resultado = ""

        if pelea >= 20:

            resultado = "está desequilibrada"

        else:

            resultado = "está equilibrada"



        logging.info(f"El heroe {heroe.nombre} {heroe.apellidos} con un poder de {heroe.puntuacionTotal} se ha enfrentado "
                     f"al villano {villano.nombre} {villano.apellidos} con un poder de {villano.puntuacionTotal} "
                     f"en una pelea que {resultado}.")

        return resultado


