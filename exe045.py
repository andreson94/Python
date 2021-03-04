#importando modolo random especifico
from random import randint
from time import sleep
opcoes = ('PEDRA','PAPEL','TESOURA') #ITENS DO MENU
cpu = randint(0,2)

print('\033[1;33m===== JOKENPO =====\033[m')
#MENU DE JOGO
print('''\033[36mEscolha uma jogada: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

player = int(input('Qual sua opção: '))
print('\033[1;33m JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[1;33m=-=\033[m' * 7 )
print('''\033[34mplayer jogou: {}
cpu jogou: {}'''.format(opcoes[player],opcoes[cpu]))
print('\033[1;33m=-=\033[m' * 7)

if cpu == 0: #computador jogou pedra
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('\033[1;32mPLAYER WINS')
    elif player == 2:
        print('\033[1;31mCPU WINS')
    else:
        print('OPÇÃO INVALIDA')
elif cpu == 1: #CPU JOGOU PAPEL
    if player == 0:
        print('\033[1;31mCPU WINS')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('\033[1;32mPLAYER WINS')
    else:
        print('OPÇÃO INVALIDA')
elif cpu == 2: #CPU JOGOU TESOURA
    if player == 0:
        print('\033[1;32mPLAYER WINS')
    elif player == 1:
        print('\033[1;31mCPU WINS')
    elif player == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVALIDA')
