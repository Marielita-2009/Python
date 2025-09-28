Algoritmo supermercado 
	Escribir "Ingrese el nombre del cliente"
	Leer nom 
	Dimension lista_productos[10,2]
	
	Para x=1 Hasta 5 Con Paso 1 Hacer
		Escribir ""
		Escribir "-----Catálogo-----" 
		Escribir "Arroz - Precio 1250" 
		Escribir "Frijoles - Precio 1320" 
		Escribir "Yogurt - Precio 880" 
		Escribir "Cereal - Precio 1190" 
		Escribir "Sal - Precio 560" 
		
		Escribir ""
		Escribir "Ingrese el nombre del artículo" 
		Leer articulo 
		Escribir "Ingrese el precio del articulo" 
		Leer precio 
		
		total = total + precio 
		
		lista_productos[x,1] = articulo 
		lista_productos[x,2] = Convertiratexto (precio)
		
		Si total > 10000 Entonces
			descuento = total * 0.10 
			total = total - descuento
			Escribir "Se aplica un descuento del 10% y el total de la compra es " total
		SiNo
			Escribir "Total a pagar ", total 
		Fin Si
	Fin Para
FinAlgoritmo
