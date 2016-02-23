import math

def combinacoes(x,y):
    comb = math.factorial(x)/(math.factorial(y) * math.factorial(x-y))
    return comb

n = int(input("Informe o número total de alunos na turma:"))
m = int(input("Informe um número de alunos num grupo:"))

print("Existem",combinacoes(n,m),"combinações possíveis!")