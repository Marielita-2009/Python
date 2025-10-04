# Ejercicio 1
# while esté activo hasta que el numero ingresado no sea igual al de la variable

import random

numero_suerte = random.randint(1,100)
numero_usuario = 0

while numero_suerte != numero_usuario:
    numero_usuario = int(input("ingrese un numero"))
    if numero_usuario >= 100:
        print("el numero ingresado es mayor a 100")
    elif numero_usuario > numero_suerte:

        if (numero_usuario - numero_suerte ) >= 20:
            print("EL Numero ingreso es muy alto")
        elif (numero_usuario - numero_suerte ) >= 10:
            print("EL Numero ingreso es alto")
        elif (numero_usuario - numero_suerte ) < 10:
            print("EL Numero ingresado esta altito")

    elif numero_usuario < numero_suerte:

        if (numero_suerte -numero_usuario ) >= 20:
            print("EL Numero ingreso es muy bajo")
        elif (numero_suerte -numero_usuario ) >= 10:
            print("EL Numero ingreso es bajo")
        elif (numero_suerte -numero_usuario ) < 10:
            print("EL Numero ingresado esta bajito ")

    else:
        print("Usted no ingreso un numero")
    


print(f"usted gano el numero era el {numero_suerte}")
