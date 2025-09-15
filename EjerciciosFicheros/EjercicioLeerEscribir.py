from datetime import datetime as date

fecha = date.now().strftime("%d%m%y")

fichero_nuevo = f"{fecha}_Personas.log"

with open ("Libro2.txt", "r")as f:
    with open (fichero_nuevo, "w")as fn:

        linea = f.readline()
        id_persona = 1
        while linea:

            print(linea, end="")
            vector = linea.split()
            vector[-1]=vector[-1].strip() #quita los salto de paginas al principio y al final

            persona = (
                "INSERT INTO Personas "
                "(id, Nombre, Apellidos, edad, calle, codigo_postal, numero, movil) "
                f"VALUES ({id_persona},'{vector[0]}', '{vector[1]}', '{vector[2]}', "
                f"'{vector[3]}', '{vector[4]}', '{vector[5]}', '{vector[6]}');"
            )

            fn.write(persona + "\n")

            print(persona)

            linea = f.readline()
            id_persona+=1



