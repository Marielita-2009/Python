nums = [1, 2, 3, 4, 5]
print(nums)

strings = ["apple", "strawberry", "cherry"]
print(strings)

mixte = ["Arroz", 4, True, 4.1]
print(mixte)

primer_elemento = nums[0] #imprime el primer elemento de la lista
segundo_elemento = strings[1] #imprime el segundo elemento de la lista
ultimo_elemento = mixte[-1] #imprime el utimo elemento de la lista
long = len(mixte) #cuenta la cantidad de elementos de la lista
print(long) #se imprime la variable long

nums.append(6) #agrega un elemento al final de la lista
strings.insert(1, "orange") #inserta un nuevo elemento en la posicion 1
dato = nums.pop() #elimina el ultimo elemento de la lista
strings.remove("apple") #elimina un elemento especifico de la lista
nums.sort() #ordena la lista de manera ascendente
mixte.reverse() #le da vuelta a la lista

a = 5
b = 10
print(a > 3 and b < 5)