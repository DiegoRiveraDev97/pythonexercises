print("Vamos a determnar si es apto para donar o no")
print("por favor llene los datos a continuacion")
edad= int(input("Ingrese su edad: "))
peso= int(input("Ingrese su peso en numero entero: "))
pulso= int(input("Ingrese su pulso en numero entero: "))
plaquetas= int(input("Ingrese su nivel de plaquetas: "))
edad_exigida = 18 
edad_exigida2= 65
peso_exigido= 5
pulso_exigido=50
pulso_exigido_maximo=110
plaquetaspermitidad= 150000

if  edad >= edad_exigida or edad <= edad_exigida2:
    if peso > peso_exigido:
        print("es apto para donar sangre")
    else:                
            print("no es apto para donar sangre")
                 
    if pulso >= pulso_exigido or pulso <= pulso_exigido_maximo:
        print("es apto para donar sangre")
    else:                
        print("no es apto para donar sangre")
    if plaquetas > plaquetaspermitidad:
        print("es apto para donar sangre")
    else:                
        print("no es apto para donar sangre")