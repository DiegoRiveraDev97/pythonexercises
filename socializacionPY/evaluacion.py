print("Bienvenidos terricolas")


num1= int(input("Ingrese un numero:"))
num2= int(input("Ingrese otro numero:"))  

while num1<0:
    
 if num1%2==0 and num2%2==0:
    print("ambos numeros son pares")

 elif num1%2==0 and num2%2==0:
    print(f"{num1} es par")

 elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")

 else: 
    print("Ambos numeros son impares")
    
print("Salir del programa")