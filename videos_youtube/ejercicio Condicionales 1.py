
#                                      JUAN DIEGO RIVERA MENESES 
#                                             FICHA: 2274935


# numeros pares o impares

num1= int(input("Insert a number:"))
num2= int(input("Insert another number:"))

if num1%2==0 and num2%2!==0:
    print("this numbers are pair")

elif num1%2==0 and num2%2==0:
    print(f"{num1} is pair")

elif num1%2!=0 and num2%2==0:
    print(f"{num2} is pair")

else: 
    print("two numbers are odd")