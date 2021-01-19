#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float (input('Quantos km percorreu? '))
dias = int (input('Por quantos dias ficou com o carro? '))
preco = (km * 0.15 ) + (dias * 60)
print(' você pagará R$ {:.2f} por {} dias e {:.0f}km rodados'.format(preco,dias,km))
