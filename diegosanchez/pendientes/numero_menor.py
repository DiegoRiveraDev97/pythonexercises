

print("Digite tres números para calcular el menor")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < num2:
    if num1 < num3:
        numero_menor = num1
    else:
        numero_menor = num3
elif num2 < num3:
    numero_menor = num2
else:
    numero_menor = num3

print("El número menor es: ", numero_menor)
