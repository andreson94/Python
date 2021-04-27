num = ('Zero','um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
       'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    n = int( input('Digite um numero entre 0 e 20 ou [-1] para sair: '))
    if n < 0 or n > 20:
        continue

    else:
        print(f'{n} por extenso escreve: \033[1;34m{num[n]}\033[m')