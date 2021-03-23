from random import shuffle
import string
palavraSecreta = ['cabeçuda','Andressa','Andreson','jubileu','miguel','gael']
shuffle(palavraSecreta)
digitadas = []
chance = 4
print('\033[1;33m=-=\033[m' * 10)
print('\033[1;34mADIVINHA A PALAVRA\033[m'.center(40))
print('\033[1;33m=-=\033[m' * 10)

while True:

    letra = input('\033[1mdigite uma letra:\033[m ').lower()

    if len(letra) > 1:
        print('\033[1;31mDigite somente uma letra!\033[m')
        continue

    digitadas.append(letra)

    if letra in palavraSecreta[0]:
        print('\033[1m_\033[m' * 30)
        print(f'A letra "{letra}" está certa!')
    else:
        print('\033[1m_\033[m' * 30)
        print(f'A letra"{letra}" não existe, você errou!\ntentativas restantes {chance}')
        digitadas.pop()
        chance += -1
        if chance == 0:
            print('\033[1;31mVocê perdeu!\033[m')
            break
        else:
            continue

    letra_temp = ''
    for letra_secreta in palavraSecreta[0]:
       if letra_secreta in digitadas:
           letra_temp += letra_secreta

       else:
           letra_temp += '*'
    print(letra_temp)
    if letra_temp == palavraSecreta[0] :
        print(f'Voce ganhou!\nA palavra {letra_temp}')
        break
