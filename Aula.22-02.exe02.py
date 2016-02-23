def status (m):
    if m >= 6:
        return 'Aprovado!'
    elif 4 <= m < 6:
        return 'VS'
    else:
        return 'REPROVADO!'

media = float(input("Entre com a média do aluno:"))
print(status(media))