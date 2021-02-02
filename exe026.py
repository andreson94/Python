nome = str(input('nome completo: ')).strip().upper()
print('A letra A aparece {}'.format(nome.count('A')))
print('Ela aparece primeiro na posição {}'.format(nome.find('A')+1))

print('Ela aparece por ultimo na posição {}'.format(nome.rfind('A')+1))
