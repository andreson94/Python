# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.


print('Descubra se 3 retas distintas podem formar um triangulo!')
a = float(input('Digite o cumprimento da reta '))
b = float(input('Digite o cumprimento da reta '))
c = float(input('Digite o comprimento da reta '))

#testando a formula
if b + c > a and a + c > b and a + b > c:
    print('Formam um triangulo')
else:
    print('não formam um triangulo')
