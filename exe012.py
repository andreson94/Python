preco = float(input('insira o preço:'))
desc = preco * float(input('insira desconto: '))/100
precofinal = preco - desc

print('o reço do produto é igual a {}'.format(precofinal))