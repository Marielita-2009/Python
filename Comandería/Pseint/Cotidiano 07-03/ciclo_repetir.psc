Algoritmo ciclo_repetir
	v = falso 
	Repetir
		Escribir "es Saprisa el mejor equipo si/no"
		Leer resp
		Borrar pantalla
		si resp == "si" Entonces
			v = verdadero
		FinSi
	Hasta Que v = verdadero 
FinAlgoritmo
