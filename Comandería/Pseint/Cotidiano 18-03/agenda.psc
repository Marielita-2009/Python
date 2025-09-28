Algoritmo agenda
	
	Dimension libreta[5,3]
	
	Para x=1 Hasta 5 Con Paso 1 Hacer
		Borrar Pantalla
		Escribir "Ingrese su nombre"
		Leer nombre 
		Escribir "Ingrese su correo" 
		Leer correo
		Escribir "Ingrese su nro.telefonico"
		Leer telefono 
		libreta[x, 1] = nombre
		libreta[x, 2] = correo 
		libreta[x, 3] = telefono
		
		Para x=1 Hasta 5 Con Paso 1 Hacer
			Para i = 1 Hasta 3 Con Paso 1 Hacer
				Escribir sin saltar x, " ", libreta[x, i]
			Fin Para
		Fin Para
	Fin Para
	
FinAlgoritmo