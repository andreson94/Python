from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
maior = n[1]
menor = n[1]
for c in n:
    if maior < c:
        maior = c

    if menor > c:
        menor = c

print(f'Os numeros sorteados foram: {n} \nO maior foi {maior} \nO menor foi {menor}')
