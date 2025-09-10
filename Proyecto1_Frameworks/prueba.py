print("Hola")
resultado = 20

print((resultado))

import calcukadora as cal

resultado = "hola"
a = float(input("dame un numero"))
a = a + 10

print(a)


# no se puede llamar a un metodo antes de crearlo
def miPrimerMetodo():
    nombre = "Francisco"
    print(nombre)
    apellido = "Alia"
    print(apellido)


cal.sumar()

if a > 20:
    print("hola")
    if a > 100:
        print("Estas jodido")
    elif a < 100:
        print("Estas bien")
else:
    print("adios")
