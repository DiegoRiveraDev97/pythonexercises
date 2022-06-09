
#                                      JUAN DIEGO RIVERA MENESES 
#                                             FICHA: 2274935

# programa que solicite el radio de un circulo 
# con su area asignada  y la longitud de la circunferencia 
#
import math 

radius= float(input("radius => "))

area=math.pi * radius**2
length = 2 * math.pi * radius

print(f"The area is: {area:.3f}")
print(f"la length of the circumference es: {length:.3f}")