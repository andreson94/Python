#Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

print('\033[1;34mConversor de Numeros\033[m')
num = int(input('\033[1;31mDigite um numero inteiro:\033[m '))
print('''Escolha uma das opções para conversão
[1] \033[1mBinario\033[m
[2] \033[1mOctal\033[m
[3] \033[1mHexadecimal\033[m''')
#escolhendo opção
opcao = int(input('\033[1;31mDigite uma opção:\033[m '))
if opcao == 1:
    print('O numero \033[1;34m{}\033[m convertido para Binario é \033[1;32m{}\033[m'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O numero \033[1;34m{}\033[m convertido para Octal é \033[1;32m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero \033[1;34m{}\033[m convertido para Hexadecimal é \033[1;32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mNumero invalido!\033[m')