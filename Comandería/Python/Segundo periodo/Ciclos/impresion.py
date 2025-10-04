suma_total = 0 
contador_articulos = 0 

while True:
    entrada = input("Ingrese el precio del articulo o escriba -fin- para terminar: ")
    if entrada.lower() == "fin":
        break
    elif entrada != "fin":
        suma_total += float(entrada)
        contador_articulos += 1

print(f"El total de los gastos es {suma_total}, usted a comprado {contador_articulos} artículos")