lista=[]

for i in range (5):
    valor=int(input("Escriba un numero: "))
    lista.append(valor)
    if lista [i]<0:
        lista [i]=int(input("Escriba un numero positivo: "))
print(lista)        