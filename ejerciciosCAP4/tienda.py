

#Este es el simbolo para comentarios de python

compra = int(input("Ingrese el valor total de la compra: "))
balota = input("Cual fue el color de su balota?")
roja = ("Tiene el 100% del descuento")
verde = compra-(compra*0.5)
blanco = compra-(compra*0.3)
negro = compra-(compra*0.2)
amarillo = compra-(compra*0.1)

if compra >= 50000 :
   if balota == ("roja"): 
    print("Tienes el 100% del descuento: ")
   elif balota == ("verde"):
    print("tienes el 50% del descuento")
   elif balota == ("blanco"):
    print("Tienes el 30% del descuento: ")
   elif balota == ("negro"):
    print("tienes el 20% del descuento")
   elif balota == ("amarillo"):
    print("Tienes el 10% del descuento: ")
else:
  print(f"no aplica descuento y el valor a pagar es:{compra} ")



