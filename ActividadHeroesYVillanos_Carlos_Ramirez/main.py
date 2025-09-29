import logging
import random

import log
from clases.factoria import PersonaFactoria

def menu():
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Para enfrentar un heroe a un villano")
    print("5) Para salir")


def gestionAulaDeHeroesYVillanos(opcion, heroes, villanos):
    match opcion:
        case 1:
            heroe = PersonaFactoria.crearHeroe()
            heroes.append(heroe)
            return f"Héroe {heroe.nombre} {heroe.apellidos} creado."
        case 2:
            villano = PersonaFactoria.crearVillano()
            villanos.append(villano)
            return f"Villano {villano.nombre} {villano.apellidos} creado."
        case 3:
            atributo = input("Dime el atributo para filtrar: ")
            valor_buscado = input("Dime el valor a buscar: ")

            filtroHeroes = PersonaFactoria.getPersonajeByAtributo(heroes, atributo, valor_buscado)
            filtroVillanos = PersonaFactoria.getPersonajeByAtributo(villanos, atributo, valor_buscado)

            resultado_busqueda = []
            resultado_busqueda.append(filtroHeroes)
            resultado_busqueda.append(filtroVillanos)

            return resultado_busqueda
        case 4:

            aleatorio1 = random.randint(0, len(heroes)-1)
            aleatorio2 = random.randint(0, len(villanos)-1)

            heroe_aleatorio = heroes[aleatorio1]
            villano_aleatorio = villanos[aleatorio2]


            resultadoPelea = PersonaFactoria.enfrentarse(heroe_aleatorio, villano_aleatorio)

            return resultadoPelea

        case _:

            return "Hasta luego Lucas"


def main():

    heroes = []
    villanos = []

    try:
        while True:
            menu()
            opcion = int(input("¿Qué eliges? "))
            if opcion >= 6:

                logging.warning(f"La opción seleccionada {opcion} no existe.")
                print("Selecciona una opción válida")
            else:
                resultado = gestionAulaDeHeroesYVillanos(opcion, heroes, villanos)
                print(resultado)

    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"Error inesperado: {e}")




if __name__ == "__main__":
    main()