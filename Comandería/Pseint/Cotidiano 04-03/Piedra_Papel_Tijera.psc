Algoritmo Piedra_Papel_Tijera
	Definir usuario, PC Como entero 
	PC =azar(3)+1  
	Escribir "escoja" 
	Escribir "1 - Pierda" 
	Escribir "2 - Tijeras"
	Escribir "3 - papel" 
	Leer usuario
	
	Si pc = usuario Entonces
		Escribir "empate" 
	SiNo
		Si pc = 1 y usuario = 2 Entonces
			Escribir "La PC gana, usted escogio tijeras y la pc piedra" 
		SiNo
			Si pc = 2 y usuario = 1  Entonces
				Escribir "El usuario gana, la pc escogio tijeras y usted escogio piedra" 
			SiNo
				Si pc = 1 y usuario = 3 Entonces
					Escribir "El usuario gana, la pc escogio piedra y usted escogio papel"
				SiNo
					Si pc = 3 y usuario = 1 Entonces
						Escribir "La PC gana, usted escogio piedra y la pc escogio papel" 
					SiNo
						Si pc = 2 y usuario = 3 Entonces
							Escribir "La PC gana, usted escogio papel y la pc tijeras" 
						SiNo
							Si pc = 3 y usuario = 2 Entonces
								Escribir "El usuario gana, la pc escogio papel y usted escogio tijeras"
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
