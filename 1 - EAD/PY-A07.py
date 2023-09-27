'''
Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
O programa deve fornecer as seguintes funcionalidades:
Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos
números de matrícula. O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
'''

cad_alunos = {}


def adicionar_aluno():
    print('> Adicionar aluno')
    nome = input('Nome: ')
    matricula = input('Matricula: ')
    global cad_alunos
    cad_alunos[matricula] = nome
    print('Aluno adicionado com sucesso!\n')


def remover_aluno():
    print('> Remover aluno')
    matricula = input('Matricula: ')
    global cad_alunos
    if matricula in cad_alunos:
        r = input(f'Deseja realmente remover o aluno {cad_alunos[matricula]}? ("S" ou "N")\nR: ')
        if r == 'S':
            del cad_alunos[matricula]
            print('Aluno removido com sucesso!\n')
        else:
            print('Remoção cancelada.\n')
    else:
        print('Esse aluno encontrado!\n')


def visualizar_todos():
    global cad_alunos
    for aluno in cad_alunos:
        print(f'Nome: {cad_alunos[aluno]}, Matrícula: {aluno}')
    print('\n')


while True:
    opcao = input('-- Cadastro de alunos\n'
                  '1 - Adicionar\n'
                  '2 - Remover\n'
                  '3 - Visualizar todos\n'
                  '4 - Sair\n'
                  'R: ')
    if opcao == '4':
        break
    elif opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        remover_aluno()
    elif opcao == '3':
        visualizar_todos()
    else:
        print('Opção inválida! Tente novamente.')
