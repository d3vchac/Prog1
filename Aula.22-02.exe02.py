def status(m):
    if m >= 6:
        return 'Aprovado!'
    elif 4 <= m < 6:
        return 'VS'
    else:
        return 'REPROVADO!'

"""def sum(n):
    soma = 0
    for i in range(n):
        soma = soma + eval(input("Insira a nota:"))
    return soma


def mediaFinal(sum, n):
"""



media = eval(input("Entre com a média do aluno:"))
print(status(media))
