print('\033[1;33m===== Calculadora =====\033[1;34m')
calc = True
while calc:

    n1 = input('Digite um numero: ').strip()
    n2 = input('Digite um numero: ').strip()
    op = input('Digite orador ou [s] para sair: ').strip()

    if not n1.isnumeric() or not n2.isnumeric():
        print('VOCE PRECISA DIGITAR UM NUMERO!')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if op != 's':
        # recebendo operadores -+/*
        if op == '-':
            print(n1 - n2)

        elif op == '+':
            print(n1 + n2)

        elif op == '*':
            print(n1 * n2)

        elif op == '/':
            print(n1 / n2)
    else:
        calc = False
        break
