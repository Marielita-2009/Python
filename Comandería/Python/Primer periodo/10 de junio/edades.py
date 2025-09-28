edad = int(input("Ingrese su edad:"))
mayor_edad = edad >= 18
tiene_licencia = True
if tiene_licencia == mayor_edad:
    print("Puede conducir, su edad es:", edad)
else:
    print("Usted es menor de edad, no puede conducir")