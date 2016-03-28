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
    m = txt_mtz(nomeArq)

    continua = 's'
    while continua == 's' or continua == 'S':
        if continua == 's' or continua == 'S':
            aluno = input('Digite o nome do aluno:')

            for i in range(len(m)):
                if m[i][0] == aluno:
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2])

        else:
            break
        continua = input('Deseja consultar registro de outro aluno? \n(s ou n):')

    return

def edita_registro(nomeArq):
    m = txt_mtz(nomeArq)
    continua = 's'
    while continua == 's' or continua == 'S':
        if continua == 's' or continua == 'S':
            aluno = input('Digite o nome do aluno a ser editado:')
            for i in range(len(m)):
                if m[i][0] == aluno:
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2])
                    ind = i

                    print('\n\nO que deseja editar?')
                    print('(1) Nome')
                    print('(2) Nota 1')
                    print('(3) Nota 2')
                    print('(0) Sair')
                    edit = int(input('Opção:'))

                    if edit == 1:
                        novoNome = input('Digite o novo nome:')
                        m[ind][0] = novoNome
                    elif edit == 2:
                        novaNota1 = input('Digite a nova nota 1:')
                        m[ind][1] = novaNota1
                    elif edit == 3:
                        novaNota2 = input('Digite a nova nota 2:')
                        m[ind][2] = novaNota2
                    elif edit == 0:
                        break
                    else:
                        print('Opção inválida!')
                        break

        else:
            break
        continua = input('Deseja editar outro aluno? ( s (sim) ou n (não) ) \n')

    mtz_txt(m,nomeArq)

    return

def apaga_registro(nomeArq):
    m = txt_mtz(nomeArq)
    continua = 's'
    while continua == 's' or continua == 'S':
        if continua == 's' or continua == 'S':
            aluno = input('Digite o nome do aluno a ser apagado:')
            for i in range(len(m)):
                if m[i][0] == aluno:
                    print('Tem certeza que deseja apagar o registro de',m[i][0],'?')
                    resp = input('(s ou n):')

                    if resp.capitalize() == 'S':
                        m.pop(i)
                    elif resp.capitalize() == 'N':
                        break
                    else:
                        print('Opção inválida!')
                        break

        else:
            break
        continua = input('Deseja apagar registro de outro aluno? \n( s (sim) ou n (não) ): ')

    mtz_txt(m,nomeArq)

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

def medias(nomeArq):
    m = txt_mtz(nomeArq)
    continua = 's'
    while continua == 's' or continua == 'S':
        if continua == 's' or continua == 'S':
            print('Deseja consultar qual média?')
            print('(1) Aluno')
            print('(2) Prova 1')
            print('(3) Prova 2')
            print('(4) Geral')
            opt = eval(input('Opção:'))

            #Média da primeira prova
            med1 = 0
            soma1 = 0
            for i in range(len(m)):
                soma1 += float(m[i][1])
            med1 = soma1/len(m)

            #Média da segunda prova
            med2 = 0
            soma2 = 0
            for i in range(len(m)):
                soma2 += float(m[i][2])
            med2 = soma2/len(m)

            #Opções
            if opt == 1:
                aluno = input('Digite o nome do aluno:')
                for i in range(len(m)):
                    if m[i][0] == aluno:
                        print('A média de',m[i][0],'é:',((float(m[i][1])+float(m[i][2]))/2))
            elif opt == 2:
                print('A média da prova 1 é:',med1)
            elif opt == 3:
                print('A média da prova 2 é:',med2)
            elif opt == 4:
                print('A média geral é:',((med1 + med2)/2))
            else:
                print('Opção inválida!')
                break

        else:
            break
        continua = input('\nDeseja consultar outra média? \n( s (sim) ou n (não) ):')


    return

def listar(nomeArq):
    m = txt_mtz(nomeArq)
    continua = 's'
    while continua == 's' or continua == 'S':
        if continua == 's' or continua == 'S':

            print('Selecione a opção de desejada:')
            print('(1) Listar do arquivo')
            print('(2) Listar por ordem alfabética')
            print('(3) Listar por ordem alfabética inversa')
            print('(4) Listar por maior nota na prova 1')
            print('(5) Listar por menor nota na prova 1')
            print('(6) Listar por maior nota na prova 2')
            print('(7) Listar por menor nota na prova 2')
            print('(0) Sair')
            op = eval(input('Opção:'))


            if op == 1:
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
            elif op == 2:
                m.sort(key=lambda x:x[0])
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
                s = input('Gostaria de gravar dessa forma no aquivo? \n(s ou n):')
                if s.capitalize() == 'S':
                    mtz_txt(m,nomeArq)

            elif op == 3:
                m.sort(key=lambda x:x[0],reverse=True)
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
                s = input('Gostaria de gravar dessa forma no aquivo? \n(s ou n):')
                if s.capitalize() == 'S':
                    mtz_txt(m,nomeArq)

            elif op == 4:
                m.sort(key=lambda x:float(x[1]),reverse=True)
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
                s = input('Gostaria de gravar dessa forma no aquivo? \n(s ou n):')
                if s.capitalize() == 'S':
                    mtz_txt(m,nomeArq)

            elif op == 5:
                m.sort(key=lambda x:float(x[1]))
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
                s = input('Gostaria de gravar dessa forma no aquivo? \n(s ou n):')
                if s.capitalize() == 'S':
                    mtz_txt(m,nomeArq)

            elif op == 6:
                m.sort(key=lambda x:float(x[2]),reverse=True)
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
                s = input('Gostaria de gravar dessa forma no aquivo? \n(s ou n):')
                if s.capitalize() == 'S':
                    mtz_txt(m,nomeArq)

            elif op == 7:
                m.sort(key=lambda x:float(x[2]))
                for i in range(len(m)):
                    print('Nome:',m[i][0])
                    print('Nota 1:',m[i][1])
                    print('Nota 2:',m[i][2],'\n')
                s = input('Gostaria de gravar dessa forma no aquivo? \n(s ou n):')
                if s.capitalize() == 'S':
                    mtz_txt(m,nomeArq)

            elif op == 0:
                break

            else:
                print('Opção inválida!')
        else:
            break
        continua = input('Deseja listar de outra forma? \n( s (sim) ou n (não) ): ')
    return

def menu_principal():
    print('Escolha uma das opções abaixo:')
    print('(1) Selecionar arquivo')
    print('(2) Criar arquivo')
    print('(0) Sair')
    opt = eval(input('Opção:'))

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
    opt = eval(input())

    if opt == 1:
        consulta_aluno(n)
        menu_sec(n)
    elif opt == 2:
        edita_registro(n)
        menu_sec(n)
    elif opt == 3:
        apaga_registro(n)
        menu_sec(n)
    elif opt == 4:
        maior_nota(n)
        menu_sec(n)
    elif opt == 5:
        menor_nota(n)
        menu_sec(n)
    elif opt == 6:
        medias(n)
        menu_sec(n)
    elif opt == 7:
        listar(n)
        menu_sec(n)
    elif opt == 8 or opt == 0:
        menu_principal()
    else:
        print('Opção inválida!')
        menu_sec(n)



#      PROGRAMA PRINCIPAL      #
menu_principal()
