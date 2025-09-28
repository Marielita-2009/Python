Algoritmo cambio_moneda
	Definir moneda como real 
	Escribir "Seleccione la conversion a la moneda que quiere realizar" 
	Escribir "1 - para dolares"
	Escribir "2 - para euros"
	Escribir "3 - para libras"
	Leer moneda 
	
	Definir monto como entero 
	Escribir "Ingrese el monto en colones que desea convertir" 
	Leer monto 
	
	Segun moneda Hacer
		1:
			Escribir "Cambio de colones a dolares " monto / 506
		2:
			Escribir "Cambio de colones a euros " monto / 548 
		3:
			Escribir "Cambio de colones a libras " monto / 647,82
		De Otro Modo:
			Escribir "El cambio es invalido"
	Fin Segun
	
FinAlgoritmo
