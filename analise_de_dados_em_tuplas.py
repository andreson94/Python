n = (int(input('Digite um numero:')),
     int(input('Digite um numero:')),
     int(input('Digite um numero:')),
     int(input('Digite um numero:')))

print(f'os valores digitos foram {n}')
print(f'o numero 9 apareceu {n.count(9)}x')
if 3 in n:
    print(f'o numero 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('o numero 3 nao foi digitado em nenhuma posição')

print(f'os numeros pares foram ')
for c in n:
    if c % 2 == 0:
        print(c)