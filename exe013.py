salario = float(input('salario anterior: R$ '))
almento = salario * float(input('Porcentagem de almento: '))/100
novo = salario + almento
print('O novo salario é R${:.2f}'.format(novo))