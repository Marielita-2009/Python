#def nombre_de_la_funcion (parametro1, parametro2)
    #codigo la funcion
#f es para darle formato al texto

def saludar(nombre):
    mensaje = f"Hola, {nombre}"
    print(mensaje)

saludar("Juan")

def suma(a, b):
    resultado = a + b
    return resultado 

resultado = suma(5, 5)
print(resultado)

def area_rectangulo(base, altura):
    area = base + altura 
    return area

base = int(input("Ingrese el valor de la base del rectangulo: "))
altura = int(input("Ingrese el valor de la altura del rectangulo: "))

area = area_rectangulo(base, altura)
print(area)

#argumento: dato que se ingresa
#parámetro: variable definida 

print(dir(__builtins__))
help(print)