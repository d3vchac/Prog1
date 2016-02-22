import random

um = dois = tres = quatro = cinco = seis = 0
num = []

for i in range(10):
    num.append(random.randint(1,6))
    if num[i]==1:
        um += 1
    elif num[i]==2:
        dois += 1
    elif num[i]==3:
        tres += 1
    elif num[i]==4:
        quatro += 1
    elif num[i]==5:
        cinco += 1
    elif num[i]==6:
        seis += 1

print(num)

vezes = []
vezes.append(um)
vezes.append(dois)
vezes.append(tres)
vezes.append(quatro)
vezes.append(cinco)
vezes.append(seis)

print(vezes)
