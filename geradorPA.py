print('GERADOR PA')
print('=-=' * 8)
termo1 = int(input('1º termo: '))
razao = int(input('Razãp: '))
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while cont <= total:
        print(f'{termo1} -> ', end='')
        termo1 += razao
        cont += 1
    print('Pausa')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
