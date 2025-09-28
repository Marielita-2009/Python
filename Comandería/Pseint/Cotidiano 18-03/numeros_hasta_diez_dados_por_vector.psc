Algoritmo numeros_hasta_diez_dados_por_vector
	dimension numeero[10]// le doy limite a mi lista 
	Para x=1 Hasta 10 Con Paso 1 Hacer
		Escribir "Ingrese un numero "
		leer numerito
		numeero[x] = numerito// almaceno numero de mi vector  
		
	Fin Para  
	Para x=1 Hasta 10 Con Paso 1 Hacer
		escribir x," - ",numeero[x] //muestro la lista de numeros 
	Fin Para
	Para x=1 Hasta 10 Hacer
		suma = suma + numeero[x] 
		
	Fin Para
	Escribir " el total de la suma es " suma 
FinAlgoritmo
