fruits = ["apple", "banana", "cherry", "melon"]
fruits[0]
fruits.append("kiwi")
fruits.insert(2, "pera")
fruits.remove("kiwi")
print(fruits)

lista = [3,1,4,1,5,9,2,6,5,3,5]
lista.sort()
print(lista)

nueva_lista = sorted(lista)

rango = range(0,10,2) #eficiencia del uso de la memoria al crear una memoria
lista_rango = list(range(0,10,2))
for i in range (5):
    print(i)

esta_rango = 3 in range(0,5)
