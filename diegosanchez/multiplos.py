


from re import A


print("Ahora vamos a calcular los numeros multiplos del valor que se ingrese")

a = int(input("Ingrese un numero para saber su multiplo: "))
b = int(input("Ingrese el numero para la cantidad a sacar del multiplo: "))

def muestre_multiplos(a,b):
    return [a * i for i in range(1,b + 1)]
print(muestre_multiplos(a,b))
