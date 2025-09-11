
# Ejercicio 1: Lista de equipos

# Crea una lista con los 5 primeros equipos de la clasificación (puedes inventar el orden).

lista = ['Osasuna', 'Mallorca', 'Betis', 'Celta', 'Oviedo']

# Muestra en pantalla el primer y último equipo.

print(lista[0])
print(lista[-1])

# Añade un equipo nuevo al final de la lista.

lista.append('Rayo')

# Inserta a mano un equipo en la primera posición.

lista.insert(1, 'Elche')

# Elimina un equipo que ya no quieras que esté en la lista.

del lista[3]

# Ejercicio 2: Jornada de partidos
#
# Crea dos listas:
# locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
# visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]
# imprimir los partidos en formato:
# Real Madrid vs Athletic
# Barcelona vs Betis

locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]

salido = False

for local in locales:

    for visitante in visitantes:

        if locales.index(local) == visitantes.index(visitante):
            print(local + ' vs ' + visitante)

#Elimina un partido (por ejemplo, el de Sevilla vs Villarreal).

del locales[3]
del visitantes[3]

#Añade un nuevo partido con un equipo inventado.

locales.append('Alavés')
visitantes.append('Manechego')

for local in locales:
    for visitante in visitantes:

        if (locales.index(local) == visitantes.index(visitante)):
            print(local + ' vs ' + visitante)


# Ejercicio 3: Clasificación de goleadores
# Crea una lista con los goles de 6 jugadores:

goleadores = [4,6,10,5,3,2]

# Muestra cuántos jugadores hay

print(len(goleadores))

# Ordena la lista de goles de menor a mayor y luego de mayor a menor.

goleadores.sort()
print(goleadores)
goleadores.sort(reverse=True)
print(goleadores)

# Muestra el máximo y el mínimo de la lista (max() y min()).

print(max(goleadores))
print(min(goleadores))

# Inserta un nuevo jugador con 8 goles en la posición correcta para mantener el orden.

goleadores.insert(1,8)
print(goleadores)