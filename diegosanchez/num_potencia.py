

print("calcular las potencias de 2")


numerador = 2
exponente = int(input("digite un numer para sacar exponente: "))

def mostrar_potencias(numerador,exponente):
    resultado=1
    for i in range(exponente):
        resultado *= numerador
    return resultado

print(mostrar_potencias(numerador,exponente))