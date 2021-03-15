hora = input('Digite a hora entre 0-23: ')

if hora.isdigit():  #verificando o valor digitado
    hora = int(hora)   #fazendo a conversão para um numero inteiro

    if hora < 0 or hora > 23:
        print('Digite um horario entre 0 e 23')

    else:
        if hora <= 11:
            print('Bom dia!')

        elif hora <= 17:
            print('Boa tarde!')

        else:
            print('Boa noite!')
else:
    print('Favor digitar um horario valido!')

