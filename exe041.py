#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:

from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print('Idade do Atleta {}'.format(idade))
if idade <= 9:
    print('Sua categoria é Mirim')
elif idade <= 14:
    print('Sua categoria é Infantil')
elif idade <= 19:
    print('Sua categoria é Junior')
elif idade <= 25:
    print('Sua categoria é Senior')
else:
    print('Sua categoria é Master')