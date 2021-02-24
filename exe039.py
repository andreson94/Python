#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
# ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('ANALISE DE ALISTAMENTO MILITAR')
ano = int(input('Informe o ano de seu nascimento: '))
idade = date.today().year - ano
prazo = idade - 18
if idade >= 17 and idade <= 18:
    print('Você já tem {} anos!\nPode se alistar!'.format(idade))
elif idade < 17:
    print('Voce tem apenas {} anos é muito novo, ainda faltam {} anos '.format(idade,prazo))
else:
    print('você tem {} anos já passou da idade!\nPassaram {} anos do prazo!'.format(idade,prazo))

