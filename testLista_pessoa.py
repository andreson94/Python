pessoa = []
add_nome = 0
add_idade = 1

while True:
    sair = input('Sair [s / n]: ').strip().lower()
    if sair != 's':
        nome = input('Nome: ')
        idade = input('idade: ')
        pessoa.insert(add_nome,nome)
        pessoa.insert((add_idade),idade)
        ver = int(input('gostaria de ver quem: '))
        add_nome += 2
        add_idade += 2

        if ver != -1:
            print('=================')
            print(f'nome:{pessoa[ver]}\nidade:{pessoa[ver + 1]}')

        else:
            continue
    else:
        break

    print(add_nome, add_idade)