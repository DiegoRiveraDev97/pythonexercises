 
 #                                      JUAN DIEGO RIVERA MENESES 
#                                             FICHA: 2274935

import math
#ITERACION SIMPLE DE WHILE 
n = 2
while n<=10:
    print(n)
    n += 1
print("Ciclo terminado")  
  

#  CICLO WHILE 
num=int(input("Please insert a number"))

while num <0:
    print(f"this number is negative, insert a positive")
    num=int(input("Please insert a number again"))
else:
    print(f"This number is valid") 



# CICLO WHILE CON OPERACION MATEMATICA RAIZ CUADRADA
number= int(input("Insert a number:"))

while number<0:
    print("Alert, the number must be positive")
    number= int(input("Insert number again:"))

print(f"\nYour square root is : {(math.sqrt(number)):.2f}")
#                                                   :.2F -->LLAMA A SOLO 2 DECIMALES DE RESULTADO 
