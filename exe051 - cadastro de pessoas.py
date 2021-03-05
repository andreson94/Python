mvelho = 0
soma = 0
mul = 0
for p in range(1, 5):  #coletando informações dos clientes
    print('===== {}ª PESSOA ====='.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F : ')).strip().upper()
     soma = soma + idade
    if mvelho == 1:  #validando primeiro dado
        mvelho = idade
    else:       #testando e trocando os dados
        if idade > mvelho:
            mvelho = idade
    if sexo == 'F':
        mul = mul + 1

media = soma / p
print('Tem {} mulheres'.format(mul))
print('A média de idade é {}'.format(media))
print('O homem mais velho tem {} anos'.format(mvelho))




