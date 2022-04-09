




#Juan Diego Rivera Meneses

""" Escriba un programa en Python que acepte dos cadenas de texto y compute el producto
cartesiano letra a letra entre ellas (solución). """


cadena = input("Introduce un texto: ")
for a, b in enumerate(cadena):
    print('La palabra es: %s  -  y la posición %i' %(b,a))