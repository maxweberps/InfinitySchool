dict_alunos = {}


def adicionar_aluno():
    print('\n> Cadastro de aluno')
    matricula = input('Matricula: ')
    nome = input('Nome: ')
    dict_alunos[matricula] = nome


def remover_aluno():
    print('\n> Remover aluno')
    matricula = input('Matricula: ')
    del dict_alunos[matricula]
    print('Aluno removido com sucesso.')


def atualizar_aluno():
    print('\n> Atualizar aluno\n--')
    matricula = input('Matricula: ')
    print(f'Nome atual: {dict_alunos[matricula]}')
    dict_alunos[matricula] = input('Novo nome: ')
    print('Alteração realizada com sucesso.')


def ver_alunos():
    print('\n> Relação de alunos')
    for matricula, nome in dict_alunos.items():
        print('---------------')
        print(f'Matricula: {matricula}')
        print(f'Nome: {nome}')
    print('---------------')

    pass
