


print("1.suma\n2. resta\n3. multiplicacion\n4. division")

operacion = int(input("que operacion desea?"))
num1 = int(input("Por favor ingrese numero 1: "))
num2 = int(input("Por favor ingrese numero 2: "))


if (operacion == 1):
    print(str(num1 + num2))
elif (operacion == 2):
    print(str(num1 - num2))
elif (operacion == 3):
    print(str(num1 * num2))
elif (operacion == 4):
    print(str(num1 / num2))
else:
    print("Debe elegir una operacion")
    