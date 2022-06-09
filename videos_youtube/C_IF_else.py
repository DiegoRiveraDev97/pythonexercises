

#                                      JUAN DIEGO RIVERA MENESES 
#                                             FICHA: 2274935


# CONDICIONAES ANIDADAS

age = int(input("Enter your age :"))

if 0<age<100: #RANGO
    print("Correct age")
    if age>=18:
        print("You're of age ") # MAYOR DE EDAD
    else:
        print("you are underage")#MENOR DE EDAD
else:
    print("Incorrect age")