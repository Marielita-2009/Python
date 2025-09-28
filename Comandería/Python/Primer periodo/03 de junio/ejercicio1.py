nombre = input("Ingrese su nombre ")
tarea = input("Ingrese el nombre de la tarea ")
estado = "en progreso"
print(f"{nombre} revisando la tarea {tarea}")
if estado == "completo":
    print(f"{tarea} finalizada")
else:
    print(f"{nombre}: {tarea} aún {estado} TRABAJE")