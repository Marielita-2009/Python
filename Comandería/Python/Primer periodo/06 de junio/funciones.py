#cada funcionn va a tener entrada, proceso y salida. Finalidad? la repetición

def sumar(a, b):
    return a + b

def sumar():
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(n1 + n2)

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
resultado = sumar(n1, n2)
print(f"El resultado de la suma es: {resultado}")

sumar()