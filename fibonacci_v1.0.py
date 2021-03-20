termo = int(input('Termo a ser mostrado: '))
cont = 3
fib1 = 0
fib2 = 1

print('{} -> {} -> '.format(fib1,fib2), end='')
while cont <= termo:
    soma_fib = fib1 + fib2
    print('{} -> '.format(soma_fib), end='')
    fib1 = fib2
    fib2 = soma_fib
    cont += 1
print('FIM')