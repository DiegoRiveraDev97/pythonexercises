#import random
#random.randrange(0, 3)

print("Juega piedra, papel o tijeras")
print("   ")
player1 = input("jugador 1 cual elijes: ")
print("   ")
player2 = input("jugador 2 cual elijes: ")
if player1 == player2:
    msg = 'Empate'
    winner = 0
elif player1 == 'piedra' and player2 == 'tijeras':
    msg = 'La piedra gana'
    winner = 1
elif player1 == 'tijeras' and player2 == 'piedra':
    msg = 'La piedra gana'
    winner = 2
elif player1 == 'tijeras' and player2 == 'papel':
    msg = 'La tijeras gana'
    winner = 1
elif player1 == 'papel' and player2 == 'tijeras':
    msg = 'La tijeras gana'
    winner = 2
elif player1 == 'papel' and player2 == 'piedra':
    msg = 'El papel gana'
    winner = 1
elif player1 == 'piedra' and player2 == 'papel':
    msg = 'El papel gana'
    winner = 2

if winner == 0:
    msg = 'Empate'
else:
    msg = f'Gana persona{winner}: {msg}'
print(msg)
