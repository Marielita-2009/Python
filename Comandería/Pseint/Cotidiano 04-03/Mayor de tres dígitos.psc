Algoritmo nums
	Definir numero1, numero2, numero3 Como entero //Defino el tipo de numero
	Escribir "ingrese un numero"
	Leer numero1
	Escribir "ingrese un segundo numero" 
	Leer numero2
	Escribir "ingrese un tercer numero"
	Leer numero3 
	
	Si número1 > número2 y numero1 > numero3 Entonces
		Escribir "el mayor es " numero1
	SiNo
		Si número2 > número1 y numero2 > numero3 Entonces
			Escribir "el mayor es " numero2
		SiNo
				Escribir "el mayor es " numero3 
			Fin Si
		Fin Si
FinAlgoritmo
