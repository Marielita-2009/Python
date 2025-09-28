dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print("Primer dia: ", dias_semana[0])
print("Ultimo dia: ", dias_semana[-1])
# Intentando modificar un elemento de la tupla
dias_semana[0] = "Martes" # Esto generará un error porque las tuplas son inmutables
print("Primer dia: ", dias_semana[0])