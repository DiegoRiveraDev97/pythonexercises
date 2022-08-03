    
    
      

product = (input("Ingrese el nombre del articulo: "))
    
valor = int(input("Digite el valor del producto: "))

if valor>=1000 and valor<=2000:
    pago = valor +(valor*0.16)
    print(f"El nombre del producto es {product} y el valor a pagar es {pago}")
    
elif valor>=2100 and valor <=2500:
    pago= valor+(valor*0.17)
    print(f"El nombre del producto es {product} y el valor a pagar es {pago}")
    
elif valor>=2600 and valor<=3500:
    pago= valor+(valor*0.19)
    print(f"El nombre del producto es {product} y el valor a pagar es {pago}")
    
else:
    print(f"El producto es {product} y el valor es: {valor} no se encuentra entre los rangos")
    
    
    

    
    