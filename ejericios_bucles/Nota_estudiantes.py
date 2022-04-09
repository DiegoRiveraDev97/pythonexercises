
#Juan DiegoRivera Meneses

calificaciones = int(input("Por favor ingrese la cantidad de notas de los estudiantes: "))

cant=[]
n=0

for i in range(1,calificaciones+1):
    nota = float(input("nota estudiante: "))
    n= n+nota
    cant.append(nota)
    