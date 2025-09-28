a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int (input("Ingrese un tercer numero: "))

if a > b and a > c: 
    print("El numero mayor es:", a)
elif b > a and b > c: 
    print("El numero mayor es:", b)
elif c > a and c > b:
    print("El numero mayor es:", c)
elif a == b: 
    print("Los numeros", a, "y", b, "son iguales y mayores que", c)
elif a == c: 
    print("Los numeros", a, "y", c, "son iguales y mayores que", b)
elif b == c:
    print("Los numeros", b, "y", c, "son iguales y mayores que", a)
elif a == b and a == c and b == c: 
    print("Los numeros son iguales:", a, b, c)