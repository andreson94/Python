print('\033[1;31m  *** IMC ***\033[m')
#recebendo informações do usuario
peso = float(input('\033[34mQual o seu peso?\033[m '))
alt = float(input('\033[34mQual a sua altura? \033[m')) / 100
#fazendo calculo do imc
imc = peso / (alt ** 2)
#condicionando os resultados
if imc < 18.5 :
    print('Seu IMC é {:.1f}, voce esta abaixo do peso'.format(imc))
elif imc <= 25:
    print('IMC {:.1f} Peso ideal'.format(imc))
elif imc <= 30:
    print('IMC {:.1f} sobrepeso'.format(imc))
elif imc <= 40:
    print('IMC {:.1f} obesidade'.format(imc))
else:
    print('obesidade morbida')



