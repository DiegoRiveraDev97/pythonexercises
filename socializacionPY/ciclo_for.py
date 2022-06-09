

#Estructura principal de FOR
"""
for i in [1,2,3,"hola"]:
    print(i)("mensaje")
    
    """
    
#Ejercicio
#Presentar la tabla de multiplicar de un numero ingresado por usuario

#numero=int(input("Ingrese un numero para saber la tabla de multiplicar"))

for n in range(1,10):
    for i in range(10):
        resultado=i*n
        print(i,"x",n,"=", resultado)
    

    