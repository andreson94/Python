frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
pjunta = ''.join(palavras)
reverter = pjunta[::-1]
if reverter == pjunta:
    print('Temos um palindromo')
    print(pjunta,reverter)

else:
    print('A frase não é um palindromo')
    print(pjunta, reverter)

