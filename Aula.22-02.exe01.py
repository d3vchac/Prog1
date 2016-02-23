def fat(num):
    t=1
    for i in range(num):
        t = t*(num)
        num -= 1
    return t


def comb(x,y):
    c = fat(x)/(fat(y) * fat(x-y))
    return c

n = int(input("Informe o número total de alunos na turma:"))
m = int(input("Informe um número de alunos num grupo:"))

print("Existem",comb(n,m),"combinações possíveis!")
