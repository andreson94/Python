lista = []

while True:
    nome = input('nome: ')
    idade = input('idade: ')
    lista.insert(0,nome)
    lista.insert(1,idade)
    print(lista)
    sair = input('digite [s]air ou [c]ontinuar: ')
    if sair == 's':
        break


print(lista)
