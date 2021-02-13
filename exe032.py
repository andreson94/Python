from time import sleep
from datetime import date

print('-=-'*24)
print(' '*18,'Descubra se se o ano é BISSEXTO')
print('-=-'*24)
ano = int (input('\nDigite o ano que gostaria de analisar, digite 0 caso queira o ano atual: '))
print('\nprocessando...')
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
