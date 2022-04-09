


print("calcular las potencias de 2")
numbase = 2
exponente =int(input("digite el numero al cual desea sacar exponente: "))

def mostrar_potencias(numbase,exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= numbase
    return resultado

print(mostrar_potencias(numbase,exponente))