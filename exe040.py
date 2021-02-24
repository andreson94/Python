# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

print('\033[1;34mMedia do aluno\033[m')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('\033[1;31mMédia {}\nREPROVADO!\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('\033[1;33mMédia {}\nRECUPERAÇÃO!'.format(media))
else:
    print('\033[1;34mMédia {}\nAPROVADO!'.format(media))