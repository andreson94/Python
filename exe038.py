#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

print('\033[1;31mEscreva dois numeros inteiros!\033[m')

n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))

if n1 > n2:
    print('O primeiro é maior')
else:
    print('O segundo é maior')