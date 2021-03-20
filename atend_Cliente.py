print('Precisa de Atendimento?  ')
while True:
    resp = input('Digite [s / n]: ').strip().lower()
    if resp != 's' or resp != 'n':
        print('Resposta invalida!\nTente Novamente!')
        continue

    else:
        if resp == 's':
            resp = input('Você tem o recibo ou cartão de crédito usado na compra?\nDigite [s / n]: ').strip().lower()

            if resp == 's':
                resp = input('O produto foi aberto? ')

                if resp == 's':
                    resp = input('Todas as peças estão intactas e presente? ')

                    if resp == 's':
                        pass
                    else:
                        pass
                else:
                    pass

            else:
                pass

        else:
            break
