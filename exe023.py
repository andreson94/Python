# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

n = int(input('Digite um numero entre 0 e 9999: '))
num = str(n)
print('o numero {} tem'.format(n))
print('unidades:{}'.format(num[3]))
print('Dezendas:{}'.format(num[2]))
print('centenas:{}'.format(num[1]))
print('milhar:{}'.format(num[0]))
