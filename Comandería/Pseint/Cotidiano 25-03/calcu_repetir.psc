funcion sumar 
	Escribir "Ingrese 2 numeros" 
	Leer num1, num2 
	Escribir "La suma de los numeros es " num1+num2 
	Esperar tecla 
	Borrar Pantalla
FinFuncion 

funcion restar
	Escribir "Ingrese 2 numeros" 
	Leer num1, num2 
	Escribir "La resta de los numeros es " num1-num2 
	Esperar tecla 
	Borrar Pantalla
FinFuncion

funcion dividir
	Escribir "Ingrese 2 numeros" 
	Leer num1, num2 
	Escribir "La division de los numeros es " num1/num2
	Esperar tecla 
	Borrar Pantalla
FinFuncion

funcion multiplicar 
	Escribir "Ingrese 2 numeros" 
	Leer num1, num2 
	Escribir "La multiplicacion de los numeros es " num1*num2 
	Esperar tecla 
	Borrar Pantalla
FinFuncion

funcion salir
	Escribir "No deseas hacer nada"
	Esperar tecla 
	Borrar Pantalla
FinFuncion

Algoritmo calcu_repetir
	Repetir
		Escribir "Que desea hacer" 
		Escribir "1 - sumar"
		Escribir "2 - restar" 
		Escribir "3 - dividir" 
		Escribir "4 - multiplicar"
		Escribir "5 - salir" 
		Leer opci
		Segun opci Hacer
			1:
				sumar
			2:
				restar
			3:
				dividir 
			4: 
				multiplicar 
			5: 
				salir 
			De Otro Modo:
				Escribir "No ingreso una opcion valida" 
		Fin Segun 
	Hasta Que opci = 5 
	
	
FinAlgoritmo