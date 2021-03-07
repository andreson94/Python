frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
pjunta = ''.join(palavras)
reverter = ''
for letra in range(len(pjunta)-1, -1, -1):
    reverter += pjunta[letra]
if reverter == pjunta:
    print('Temos um palindromo')
    print(pjunta,reverter)

else:
    print('A frase não é um palindromo')
    print(pjunta, reverter)
