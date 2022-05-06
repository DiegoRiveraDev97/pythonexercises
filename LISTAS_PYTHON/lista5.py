frase = input('Por favor ingrese una frase: ')

contadorfrase = frase.split()

contadorfrase = list(map(str.upper,contadorfrase))

print (contadorfrase)

sinduplicado = set(contadorfrase)

print(sinduplicado)


