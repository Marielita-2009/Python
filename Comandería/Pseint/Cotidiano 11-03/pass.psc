Algoritmo pass
	contra = "1234"
	Repetir
		Escribir "Ingrese la contraseña"
		Leer resp
		Borrar pantalla
		si resp == "1234" Entonces 
			contra = "1234"
		FinSi
	Hasta Que contra = resp
FinAlgoritmo
