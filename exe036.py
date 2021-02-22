#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;34mSIMULAÇÃO DE FINANCIAMENTO\033[m')

valor = float(input('Qual valor do Imóvel? R$'))
salario = float(input('Qual a sua renda mensal? R$'))
tempo = int(input('Em quantos anos pretende pagar o imovel? ' ))

#validando o valor das prestações
prestacao = valor / (tempo * 12)

#validação de renda
if prestacao < (salario * 30 / 100):
    print('\033[1;32mEmpréstimo Aprovado!\033[m \nO valor das parcelas ficarão em R${:.2f}'.format(prestacao))
else:
    print('\033[1;31mEmpréstimo Negado!\033[m \nO valor das parcelas ficarão em R${:.2f} excede 30% de sua renda!'.format(prestacao))