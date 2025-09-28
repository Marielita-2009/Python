#Listas: Tipo de secuencia que contiene  elementos que pueden ser de tipos de datos diferentes
#Se encierran entre paréntesis cuadrados separados por comas
#range para crear listas con enteros consecutivos

#1. Creación y Acceso de Listas
# Crea una lista llamada frutas con los siguientes elementos: "manzana", "banana", "cereza", "dátil".
# Imprime la lista completa frutas.
#Imprime el primer elemento de la lista.
#Imprime el último elemento de la lista.
# Imprime el elemento en la posición (índice) 2 de la lista.

frutas = ["manzana", "banana", "cereza", "dátil"]
print(frutas)
print(frutas[0])
print(frutas[-1])
print(frutas[2])

#2. Modificación de Listas
#Dada la lista colores = ["rojo", "verde", "azul"]:
#Cambia el segundo elemento ("verde") por "amarillo".
#Agrega el color "morado" al final de la lista.
#Inserta el color "naranja" en la segunda posición (índice 1) de la lista.
#Imprime la lista colores después de cada modificación.

colores = ["rojo", "verde", "azul"]
colores[1] = "amarillo"
colores.append("morado")
colores.insert(1, "naranja")
print(colores)

#3. Métodos Básicos de Listas
#Dada la lista numeros = [10, 5, 20, 15, 25]:
#Usa el método .append() para añadir el número 30 al final de la lista.
#Usa el método .remove() para eliminar el número 5 de la lista.
#Usa el método .pop() para eliminar y obtener el último elemento de la lista (guárdalo en una variable y luego imprímelo).
#Usa el método .sort() para ordenar la lista de numeros de forma ascendente.
#Imprime la lista numeros después de cada operación.

numeros = [10, 5, 20, 15, 25]
numeros.append(30)
print(numeros)
numeros.remove(5)
print(numeros)
ultimo = numeros.pop(-1)
print(ultimo)
numeros.sort()
print(numeros)

#4. Longitud de una Lista y Verificación de Elementos
#Crea una lista llamada ciudades con al menos 4 nombres de ciudades.
#Usa la función len() para imprimir la cantidad de elementos en la lista ciudades.
#Verifica si la ciudad "Londres" está en tu lista ciudades usando el operador in e imprime el resultado (True o False).
#Verifica si una ciudad que no está en tu lista (ej. "Tokio") está en ella e imprime el resultado.

ciudades = ["San José", "Heredia", "Cartago", "Limón"]
print("Cantidad de ciudades", len(ciudades))
print("¿Londres está en la lista?", "Londres" in ciudades)
print("¿Tokio está en la lista?", "Tokio" in ciudades) 

#5. Listas con Diferentes Tipos de Datos
#Crea una lista llamada mixta que contenga al menos un número entero, un número flotante, una cadena de texto y un valor booleano.
#Imprime la lista mixta completa.
#Imprime el tipo de dato de cada elemento de la lista mixta usando un bucle for y la función type().
    
mixta =[4, 3.46, "Botas", False]
print(mixta)
for elementos in mixta: 
    print(type(elementos))
