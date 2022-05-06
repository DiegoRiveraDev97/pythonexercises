lista=[0,1,-3,4,-6,-10]
print("Estos numeros pasaran a ser positivos",lista)
lista=[(i>0)*i for i in lista]
print(f'estes es el resultado {lista}')