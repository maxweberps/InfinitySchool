from funcoes import *

while True:
    print('\n--- CAD ALUNO ---')
    print('Selecione uma opção: ')
    op = input(f'1 - Adicionar aluno\n'
               f'2 - Remover aluno\n'
               f'3 - Atualizar aluno\n'
               f'4 - Ver alunos\n'
               f'5 - Sair\n'
               f'R: ')
    if op == '5':
        print('\nFim.')
        break
    elif op == '1':
        adicionar_aluno()
    elif op == '2':
        remover_aluno()
    elif op == '3':
        atualizar_aluno()
    elif op == '4':
        ver_alunos()
    else:
        print('Opção inválida. Tente novamente.')
