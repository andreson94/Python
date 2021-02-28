print('===== A&A CLOTHING =====')
#RECEBENDO VALOR DA COMPRA
preco = float(input('Preço das compras: R$ '))

#MENU DE OPCAO DE PAGAMENTO
print('''FORMAS DE PAGAMENTO
[1] À VISTA / CHEQUE
[2] À VISTA NO CARTÃO
[3] PARCELADO NO CARTÃO''')
#OPCÃO DE PAGAMENTO
opcao = int(input('Qual a opção: '))
#CONDICIONANDO RESULTADOS
if opcao == 1:
    desc = preco - (preco * 10 / 100)
    print('Preço {} com 10% desconto fica R$ {:.2f}'.format(preco,desc))
elif opcao == 2:
    desc = preco - (preco * 5 / 100)
    print('Preço {} com 5% desconto fica R$ {:.2f}'.format(preco,desc))
elif opcao == 3:
    parc = int(input('''Quantas no vezes no cartão? 
    '''))
    if 2 == parc > 1:
        print('Preço a ser pago R$ {} '.format(preco))
    else:
        juros = preco + (preco * 20 / 100)
        print('O valor de {} tera 20% de juros e ficará R$ {}'.format(preco,juros))


