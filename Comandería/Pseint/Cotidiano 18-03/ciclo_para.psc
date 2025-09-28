Algoritmo ciclo_para
	dimension lista[10]
	
	Para x = 1  Hasta 10 Con Paso 1 Hacer
		Borrar pantalla 
		Escribir "Ingrese el nombre numero ", x
		leer nombre 
		lista[x] = nombre  
	Fin Para
	Para x=1 Hasta 10 Con Paso 1 Hacer
		Escribir x, " ", lista[x]
	Fin Para
FinAlgoritmo
