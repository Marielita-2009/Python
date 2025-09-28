Algoritmo vector_hastadiez
	dimension num[10]// le doy limite a mi lista 
	Para x=1 Hasta 10 Con Paso 1 Hacer
		Escribir "Ingrese un numero "
		leer numerito
		num[x] = numerito// almaceno numero de mi vector  
		
	Fin Para  
	Para x=1 Hasta 10 Con Paso 1 Hacer
		escribir x," - ",num[x] //muestro la lista de numeros 
	Fin Para
	Para x=1 Hasta 10 Hacer
		suma = suma + num[x] 
		
	Fin Para
	Escribir " el total de la suma es " suma 
FinAlgoritmo
