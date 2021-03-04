# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(2, 51, 2):

    if c % 2 == 0:
        print('\033[1;36m{}\033[m'.format(c), end = ' ')
print('acabou!')
