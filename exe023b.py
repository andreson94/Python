num = int(input('digite um numero 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('o numero {} tem'.format(num))
print('unidades:{}'.format(u))
print('Dezendas:{}'.format(d))
print('centenas:{}'.format(c))
print('milhar:{}'.format(m))