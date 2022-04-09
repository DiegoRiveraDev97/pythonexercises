

#Juan Diego Rivera Meneses


#.Diseñe un algoritmo, muestre todos los múltiplos 
# desde n hasta m siendo n y m digitados por teclado.

print("calcular los numeros multiplos")
num1 = int(input("Ingrese un numero para saber su multiplo: "))
num2 = int(input("Ingrese el numero para la cantidad a sacar del multiplo: "))

def muestre_multiplos(num1,num2):
    return [num1 * i for i in range(1,num2 + 1)]
print(muestre_multiplos(num1,num2))
