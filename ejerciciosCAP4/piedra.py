jugador1 = input("piedra, papel o tijera?: ")
jugador2 = input("piedra, papel o tijera?: ")

if jugador1 == "piedra" and jugador2 == "papel":
    print(f"GANA PAPEL")
elif jugador1 == "piedra" and jugador2 == "piedra":
    print(f"EMPATE")
elif jugador1 == "piedra" and jugador2 == "tijera":
    print(f"GANA PIEDRA")
    
elif jugador1 == "papel" and jugador2 == "piedra":
    print(f"GANA PAPEL")
elif jugador1 == "papel" and jugador2 == "papel":
    print(f"EMPATE")
elif jugador1 == "papel" and jugador2 == "tijera":
    print(f"GANA TIJERA")
    
elif jugador1 == "tijera" and jugador2 == "piedra":
    print(f"GANA PIEDRA")
elif jugador1 == "tijera" and jugador2 == "tijera":
    print(f"EMPATE")
elif jugador1 == "tijera" and jugador2 == "papel":
    print(f"GANA TIJERA")
    
    

    