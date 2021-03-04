print('10 termos de uma PA')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r #formula para saber o prdecimo termo
for c in range(t, d + r, r): #laço que vai ate o decimo termo
    print(c, end= '->')
print('acabou')