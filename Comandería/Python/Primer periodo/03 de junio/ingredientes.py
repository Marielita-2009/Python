cafe = False
mensaje = "Cappuccino listo"
if cafe: 
    print(mensaje)
elif cafe == False:
    resp = input("¿Puedes ir a comprar cafe?:  ")
    if resp == "si": 
        cafe = True
        print(mensaje)
    else: 
        print("Cappuccino en espera")
else: 
    print("Cappuccino en espera")