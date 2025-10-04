def sumar(): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))

while True:
    try:
        a = int(input("Ingresa el primer numero: n")) #Solicitamos el 1er numero al usuario
        b = int(input("Ingresa el segundo numero: n"))#Solicitamos el 2do numero al usuario
        print (("Que calculo quieres realizar entre"), (a), ("y"), (b), ("?n")) #Preguntamos el calc
        op = str(input(""" #Ofrecemos las opciones de cálculo las cuales van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir n"""))
##########################################-3-##################################################
        if op == '1':#Si el usuario elige opción 1 llamamos a sumar
            sumar()
            break
        elif op == '2':#Si el usuario elige opción 1 llamamos a restar
            restar()
            break
        elif op == '3':#Si el usuario elige opción 1 llamamos a multiplicar
            multiplicar()
            break
        elif op == '4':#Si el usuario elige opción 1 llamamos a dividir
            dividir()
            break
        else:
            print ("""Has ingresado un numero de opcion erroneo""") 
    except ZeroDivisionError:
        print("no se puede deivir por 0 no sea npc")

    except:
        print("Error")
        op = "?"

    finally:
        print ("Gracias por utilizar nuestra calculadora")


monedas = -19
if monedas >= 12:
    print (("Tienes"), (monedas), (",que es más que 12"))
elif monedas <= 12:
    print (("Tienes"),(monedas),(",que es menos que 12, lo siento consigue más monedas"))
    assert monedas < 0, "Error de comprobacion, monedas en negativo"


