n1 =int(input('Digite um numero: '))
n2 = int(input('Digite outro numreo: '))
n3 = int(input('Digite mais um numero: '))
#testando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
        maior = n3

#testando menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('-=-'*8)
print('|\033[1;32m o maior numero foi {}\033[m |'.format(maior))
print('|\033[1;31m o menor numero foi {}\033[m |'.format(menor))
print('-=-'*8)
#introduzi cores no programa usando o codigo \033[m e finalizei usando o mesmo