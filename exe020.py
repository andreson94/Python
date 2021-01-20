#import random
from random import shuffle

a1 = str(input('aluno 1'))
a2 = str(input('aluno 2'))
a3 = str(input('aluno 3'))
a4 = str(input('aluno 4'))
a5 = str(input('aluno 5'))
lista = [a1, a2, a3, a4, a5]
#random.shuffle(lista)
shuffle(lista)
print('ordem de apresentação')
print(lista)
