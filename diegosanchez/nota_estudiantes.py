

notasestudiante = int(input("ingrese el numero de notas de los estudiantes: "))
a=[]
n=0

for i in range(1,notasestudiante+1):
    nota = float(input("nota de estudiante: "))
    n=n+nota
    a.append(nota)
    