# while se usa para condiciones, mientras no se cumpla algo no ocurre la accion 

i = 0

while i <= 9:
    i += 1
    print(i)

while True:
    opc = input("""
    1 - Manzanas
    2 - Bananas
    3 - Fresas
""")
    
    if opc == "1": 
        print("Elegiste manzanas")
        break
    elif opc == "2":
        print("Elegiste bananas")
        break
    elif opc == "3":
        print("Elegiste fresas")
        break
    else:
        print("Debes elegir una opción")
