# Projeto - Agenda telefonica

agenda = {
    'Leticia': '85 99999-9998',
    'Matheus': '88 98989-3333'
}


def add_contato(nome: str, telefone: str) -> None:
    agenda[nome] = telefone
    print('Contado adicionado com sucesso!\n')
    pass


def editar_contato(nome, telefone):
    if nome in agenda:
        agenda[nome] = telefone
        print('Telefone alterado com sucesso!\n')
    else:
        print('Contato não existe!\n')


def buscar_contato(nome):
    if nome in agenda:
        print(f'{agenda[nome]}\n')
    else:
        print('Contato não existe!\n')


def deletar_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print('Contato removido com sucesso!\n')
    else:
        print('Contato não existe!\n')


def listar_todos():
    print('\n-- Contatos da agenda:')
    for contato in agenda:
        print(f'{contato}: {agenda[contato]}')


while True:
    print('--- AGENDA TELEFONICA ---')

    opcao = int(input('1 - Add contato \n'
                      '2 - Editar contato \n'
                      '3 - Buscar contato \n'
                      '4 - Deletar contato \n'
                      '5 - Listar todos \n'
                      '6 - Sair \n'
                      'Selecione uma opção: '))
    if 1 <= opcao <= 6:

        if opcao == 1:
            print('\n-- Adicionar novo contato')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            add_contato(nome, telefone)

        elif opcao == 2:
            print('\n-- Editar contato')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            editar_contato(nome, telefone)

        elif opcao == 3:
            print('\n-- Buscar contato')
            nome = input('Nome: ')
            buscar_contato(nome)

        elif opcao == 4:
            print('\n-- Deletar contato')
            nome = input('Nome: ')
            deletar_contato(nome)

        elif opcao == 5:
            listar_todos()

        elif opcao == 6:
            print('Programa encerrado.')
            break

    else:
        print('\nOpção inválida \n'
              'Tente novamente.\n')
