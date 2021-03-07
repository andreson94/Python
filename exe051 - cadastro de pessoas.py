maisvelho = 0
soma = 0
mulher20 = 0
nomevelho = 0

for p in range(1, 5):  #coletando informações dos clientes
    print('===== {}ª PESSOA ====='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F : ')).strip().upper()
    soma += idade
    if p == 1 and sexo in ('Mm'):
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        mulher20 += 1

media = soma / p
print('Tem {} mulheres maiores de idade'.format(mulher20))
print('A média de idade é {}'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maisvelho, nomevelho))




