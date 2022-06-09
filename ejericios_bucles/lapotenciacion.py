



def mostrar_potencias(numbase,exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= numbase
    return resultado
numbase = 2
exponente =int(input("digite el numero al cual desea sacar exponente: "))