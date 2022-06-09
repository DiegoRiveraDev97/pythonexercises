
#                                      JUAN DIEGO RIVERA MENESES 
#                                             FICHA: 2274935



# imprime el valor de cada elemento
for i in [1,2,3,"hola"]:
    print(i)
    



# imprime el valor de cada elemento despues de dos puntos
for i in [1,2,3,"hola",True]:
    print(i,end="..")
    
    
    # ciclo for anidado --> que imprime las tablas del 1 al 10

for n in range(1,10):
    for i in range(10):
        operation=i*n
        print(n,"x",i,"=", operation)

