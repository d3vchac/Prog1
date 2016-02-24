import sys

def menu():
    print('(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Limpar memória')
    print('(0) Sair do programa')
    print('Escolha a sua opção:')

def sum():
    a = eval(input("Entre com o primeiro número:"))
    b = eval(input("Entre com o segundo número:"))
    s = a + b
    print('O resultado é:', s)

def sub():
    a = eval(input("Entre com o primeiro número:"))
    b = eval(input("Entre com o segundo número:"))
    t = a - b
    print('O resultado é:',t)

def mult():
    a = eval(input("Entre com o primeiro número:"))
    b = eval(input("Entre com o segundo número:"))
    m = a * b
    print('O resultado é:',m)

def div():
    a = eval(input("Entre com o primeiro número:"))
    b = eval(input("Entre com o segundo número:"))
    d = a/b
    print('O resultado é:',d)

def clean_mem():

    print('desenvolvendo')

def choose_menu(opt):
    if opt == 1:
        sum()
    elif opt == 2:
        sub()
    elif opt == 3:
        mult()
    elif opt == 4:
        div()
    elif opt == 5:
        clean_mem()
    elif opt == 0:
        sys.exit()
    else:
        print('Dê uma opção válida: 1, 2, 3, 4, 5 ou 0')
    menu()


menu()
choose_menu(int(input()))
