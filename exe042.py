print('Descubra se 3 retas distintas podem formar um triangulo!')
a = float(input('Digite o cumprimento da reta '))
b = float(input('Digite o cumprimento da reta '))
c = float(input('Digite o comprimento da reta '))

#testando a formula
if b + c > a and a + c > b and a + b > c:
    print('Formam um triangulo', end='')
    #if a == b and a == c:
    if a == b == c:
        print('equilatero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('não formam um triangulo')
