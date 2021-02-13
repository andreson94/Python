#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais long
from time import sleep

n = float(input('Qual a distancia da sua viajem em km: '))
print('Processando...')
sleep(1.5)
if n > 200:
    km = n * 0.45
    print('Sua passagem sairá R${:.2f}'.format(km))
else:
    km = n * 0.50
    print('sua passagem custará R${:.2f}'.format(km))
