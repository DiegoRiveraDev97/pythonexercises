num = 17

while num >= 1:
    if num % 9 == 0:
        print(f'{num} es multiplo del 9!')
        break
    num -=1
else:
    print(f' no se encontro multiplo de 9!')