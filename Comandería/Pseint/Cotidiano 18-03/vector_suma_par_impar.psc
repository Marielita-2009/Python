Algoritmo  vector_suma_par_impar
	dimension numeero[10]// le doy limite a mi lista 
	Para x=1 Hasta 10 Con Paso 1 Hacer
		Escribir "Ingrese un numero "
		leer numerito
		numeero[x] = numerito// almaceno numero de mi vector  
		suma = suma + numerito //sumo los numeros de uno en uno en la variable suma 
		Si numerito mod 2 = 0  Entonces // comprove el numero de 2 diviendo por 2 y verificando mi residuo 
			sumapar= sumapar + numerito 
		SiNo
			sumaimpar = sumaimpar + numerito 
		Fin Si
		
	Fin Para  
	Para x=1 Hasta 10 Con Paso 1 Hacer
		escribir numeero[x] //muestro la lista de numeros del vector d uno en uno 
	Fin Para
	Escribir  "el total de suma total es " suma// muestro el total de la suma 
	escribir "el total de suma de los numeros pares es " sumapar
	escribir " el total de la suma impar es " sumaimpar 
FinAlgoritmo
	

