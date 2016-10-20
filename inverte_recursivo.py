def inverte(m,a,j):
    if j < 0:
        return ''.join(aux)
    else:
        aux.append(m[j])
        return inverte(m,aux,j-1)


num = input('DIGITE UM NÚMERO:\n') + '\n'
aux = []
print(inverte(num,aux,len(num)-1))
