









print(f"El mes con menor produccion es: {minimo}")
print(f"el promedio es: {promedio}")

for key in meses.keys():
    if (meses[key]>=promedio):
        
        print("el mes",key,"es mayor que el promedio")
        
    elif (meses[key]<=promedio):
        print(f"el mes: {key}, es menor que el promedio")