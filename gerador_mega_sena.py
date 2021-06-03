from random import randint
from time import sleep
lista = list()
jogos = list()
total = 1
cont = 0
print('*' * 49)
print('                  JOGO DA SENA')
print('*' * 49)
quant = int(input('Digite quantos jogos deseja: '))
while total <= quant:
    while True:
        num = randint(1,60)     #sortear aleatoriamente um numero inteiro entre 1 e 60
        if num not in lista:        #verifica se o numero está na lista
            lista.append(num)
            cont += 1

        if cont >= 6:       #validação para sortear somente 6 numeros
            cont = 0
            break

    lista.sort()        #organiza a lista
    jogos.append(lista[:])      #Adciona a lista dentro de outra lista
    lista.clear()       #limpa a lista para o proximo loop
    total += 1
print('*' *15, f'Sorteando {quant} jogos', '*' * 15)
sleep(0.5)
for i, j in enumerate(jogos):
    print(f'jogo {i+1}: {j}')
    sleep(1)
print('*' * 20, 'BOA SORTE', '*' * 20)
