def txt_mtz(nome):
    arq = open(nome+'.txt')
    aux = []
    mat = []
    aux.append(arq.read())
    arq.close()
    aux = aux[0].split(';')
    aux.pop(len(aux)-1)
    for i in range(len(aux)):
       mat.append(aux[i].split(','))
    for j in range(len(mat)):
        mat[j].pop(3)

    arq.close()
    return mat

def mtz_txt(matriz,nomeArq):
    arq = open(nomeArq+'.txt','w')
    for i in range(len(matriz)):
        for j in range(3):
            arq.writelines(matriz[i][j]+',')
        arq.writelines(';')
    arq.close()

"""def nome_arq():
    nome = input('Digite o nome do arquivo:')
    return nome"""

def ad_existente(nomeArq):
    print('Gostaria de adicionar outro(s) aluno(s)? \n(s ou n):')
    continua = input()
    if continua.capitalize() == 'S':
        m = txt_mtz(nomeArq)
        print('Preencha na ordem:')
        while continua.capitalize() == 'S':
            if continua.capitalize() == 'S':
                nome = input('Nome:')
                n1 = input('Nota 1:')
                n2 = input('Nota 2:')
                m.append([nome,n1,n2])
            else:
                break
            continua = input('Deseja inserir outro aluno? \n( s ou n ):')
        mtz_txt(m,nomeArq)

    return

def criar_arquivo(nomeArq):
    tab = []
    continua = 's'

    print('Preencha na ordem:')
    while continua == 's' or continua == 'S':
        if continua == 's' or continua == 'S':
            nome = input('Nome:')
            n1 = input('Nota 1:')
            n2 = input('Nota 2:')
            tab.append([nome,n1,n2])
        else:
            break
        continua = input('Deseja inserir outro aluno? ( s (sim) ou n (não) ) \n')

    mtz_txt(tab,nomeArq)

    return


def consulta_aluno(nomeArq):
    arq = open(nomeArq+'.txt')
    m = txt_mtz(nomeArq)
    aluno = input('Digite o nome do aluno:')

    for i in range(len(m)):
        if m[i][0] == aluno:
            print('Nome:',m[i][0])
            print('Nota 1:',m[i][1])
            print('Nota 2:',m[i][2])
    arq.close()
    return

def maior_nota(nomeArq):
    m = txt_mtz(nomeArq)
    maiorn1 = 0
    maiorn2 = 0
    for i in range(len(m)):
        if float(m[i][1]) > maiorn1:
            maiorn1 = float(m[i][1])
            aluno1 = i
    for j in range(len(m)):
        if float(m[j][2]) > maiorn2:
            maiorn2 = float(m[j][2])
            aluno2 = j

    print('A maior nota da prova 1 foi',maiorn1,'de',m[aluno1][0])
    print('A maior nota da prova 2 foi',maiorn2,'de',m[aluno2][0])


    if maiorn1 > maiorn2:
        print("O aluno",m[aluno1][0].rstrip('\n'),'obteve a maior nota geral, que foi:',maiorn1)
    else:
        print("O aluno",m[aluno2][0].rstrip('\n'),'obteve a maior nota, que foi:',maiorn2)


def menor_nota(nomeArq):
    m = txt_mtz(nomeArq)
    menorn1 = 10.
    menorn2 = 10.

    for i in range(len(m)):
        if float(m[i][1]) < menorn1:
            menorn1 = float(m[i][1])
            aluno_1 = i
    #for j in range(len(m)):
        if float(m[i][2]) < menorn2:
            menorn2 = float(m[i][2])
            aluno_2 = i

    print('A menor nota da prova 1 foi',menorn1,'de',m[aluno_1][0])
    print('A menor nota da prova 2 foi',menorn2,'de',m[aluno_2][0])


    if menorn1 < menorn2:
        print("O aluno",m[aluno_1][0],'obteve a menor nota geral, que foi:',menorn1)
    else:
        print("O aluno",m[aluno_2][0],'obteve a menor nota geral, que foi:',menorn2)


def menu_principal():
    print('Escolha uma das opções abaixo:')
    print('(1) Selecionar arquivo')
    print('(2) Criar arquivo')
    print('(0) Sair')
    opt = int(input('Opção:'))

    if opt == 1:
        nome = input('\nDigite o nome do arquivo:')
        ad_existente(nome)
        menu_sec(nome)
        return nome
    elif opt == 2:
        nome = input('\nDigite o nome do novo arquivo:')
        criar_arquivo(nome)
        menu_sec(nome)
        return nome
    elif opt == 0:
        print('\n\nTchau!')
    else:
        print('Opção inválida!\n\n')
        menu_principal()




def menu_sec(n):
    print('\n')
    print('Escolha uma das opções abaixo:')
    print('(1) Consultar aluno')
    print('(2) Editar registro')
    print('(3) Apagar registro')
    print('(4) Maior nota')
    print('(5) Menor nota')
    print('(6) Média')
    print('(7) Listar')
    print('(8) Trocar de arquivo')
    print('(0) Sair')
    print('\nOpção:')
    opt = int(input())

    if opt == 1:
        consulta_aluno(n)
        menu_sec(n)
    elif opt == 4:
        maior_nota(n)
        menu_sec(n)
    elif opt == 5:
        menor_nota(n)
        menu_sec(n)


    elif opt == 8 or opt == 0:
        menu_principal()




#      PROGRAMA PRINCIPAL      #
menu_principal()
