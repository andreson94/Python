palavraSecreta = 'cabeçuda'
digitadas = []

while True:

    letra = input('digite uma letra: ').lower()

    if len(letra) > 1:
        print('Digite somente uma letra!')
        continue

    digitadas.append(letra)

    if letra in palavraSecreta:
        print(f'a letra "{letra}" está certa!')
    else:
        print(f'a letra"{letra}" não existe, você errou!')
        digitadas.pop()

    letra_temp = ''
    for letra_secreta in palavraSecreta:
       if letra_secreta in digitadas:
           letra_temp += letra_secreta

       else:
           letra_temp += '*'
    print(letra_temp)
    if letra_temp == palavraSecreta :
        print(f'Voce ganhou!\nA palavra {letra_temp}')
        break
