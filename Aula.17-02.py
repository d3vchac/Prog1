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

f1 = 0
f2 = 0
f3 = 0
for i in range(6):
    if times[i]=='Brasil':
        f1 = f1 + faltas[i]
    elif times[i]=='Itália':
        f2 = f2 + faltas[i]
    elif times[i]=='Espanha':
        f3 = f3 + faltas[i]

#  Maior número de faltas:  #
if f1>f2>=f3 or f1>f3>=f2:
    print("Brasil tem maior número de faltas:",f1)
elif f2>f1>=f3 or f2>f3>=f1:
    print("Itália tem maior número de faltas:",f2)
elif f3>f1>=f2 or f3>f2>=f1:
    print("Espanha tem maior número de faltas:",f3)

#  Menor número de faltas:  #
if f3>f1>=f2 or f3>f2>=f1:
    print("Brasil tem menor número de faltas:",f1)
elif f1>f2>=f3 or f1>f3>=f2:
    print("Itália tem menor número de faltas:",f2)
elif f2>f1>=f3 or f2>f3>=f1:
    print("Espanha tem menor número de faltas:",f3)
