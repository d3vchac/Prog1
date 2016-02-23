def menu():
    print('Escolha a sua opção:')
    print('(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Limpar memória')
    print('(0) Sair do programa')

def sum(a,b):
    s = a + b
    print('O resultado é:', s)

def sub(a,b):
    t = a - b
    print('O resultado é:',t)

def mult(a,b):
    m = a * b
    print('O resultado é:',m)

def div(a,b):
    d = a/b
    print('O resultado é:',d)

def clean_mem():
    

a = eval(input("Entre com o primeiro número:"))
b = eval(input("Entre com o segundo número:"))