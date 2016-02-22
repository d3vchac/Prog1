lista = [['Brasil','Itália',[10,9]], ['Brasil','Espanha',[5,7]], ['Itália','Espanha',[7,8]]]

# Total de faltas:
soma = 0

for i in range(3):
    for j in range(2):
        soma = soma + lista[i][2][j]

print("Total de faltas no campeonato:", soma)



##########
faltas = []
times = []
for i in range(3):
    for j in range(2):
        faltas.append(lista[i][2][j])
        times.append(lista[i][j])


print(faltas)
print(times)

