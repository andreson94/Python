#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('digite um numero: '))
resto = n% 2
if resto == 0 :
    print('seu numero é PAR')
else:
    print('seu numero é IMPAR')
