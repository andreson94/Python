nome = str(input('nome completo: ')).lower().strip()
n = nome.split()
print('primeiro nome: {}'.format(n[0]))

print('ultimo nome: {}'.format(n[len(n)-1]))