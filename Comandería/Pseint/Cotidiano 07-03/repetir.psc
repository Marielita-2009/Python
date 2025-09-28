Algoritmo cardena
	
	numSecreto = azar(10)+1
	
	Repetir 
		Escribir "Ingrese el numero correcto" 
		Leer resp
		Borrar pantalla 
		Si resp = azar(10)+1 Entonces 
			numSecreto = resp 
 		FinSi
	Hasta Que numSecreto = resp
FinAlgoritmo
