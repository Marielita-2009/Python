Algoritmo calculadora 
	Definir resp como entero 
	Definir num1, num2 como real 
	Escribir "Seleccione la operación"
	Escribir "1 - sumar"
	Escribir "2 - restar"
	Escribir "3 - multiplicación"
	Escribir "4 - división"
	Leer resp
	
	Escribir "ingrese el primer numero"
	Leer num1 
	Escribir "ingrese el segundo numero" 
	Leer num2 
	
	Segun resp Hacer
		1:
			Escribir "el resultado de la suma es " num1 + num2 
		2:
			Escribir "el resultado de la resta es " num1 - num2 
		3:
			Escribir "el resultado de la multiplicacion es " num1 * num2 
		4: 
			Si num2 <> 0 Entonces
				Escribir "Resultado: ", num1 / num2
			SiNo
				Escribir "Error: no se puede dividir por cero" 
			Fin Si
		De Otro Modo:
			Escribir "No se logro realizar la operacion"
	Fin Segun
FinAlgoritmo
