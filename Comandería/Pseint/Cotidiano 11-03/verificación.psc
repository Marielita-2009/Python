Algoritmo verificación  
	Definir contra  Como Caracter 
	Definir intentos como entero 
	intentos = 0 
	Repetir
		Escribir "Ingrese la contraseña"
		Leer contra
		intentos = intentos + 1 
		si intentos >= 3 Entonces 
			Escribir "Demasiados intentos realizados"
		FinSi
		
	Hasta que contra = "1234" o intentos >= 3 
	
	si contra = "1234"
		Escribir "Contraseña correcta"
	FinSi
FinAlgoritmo

