import random

banco = [
    {'matricula': 1, 'nome': 'Leticia', 'curso': 'Java'},
    {'matricula': 2, 'nome': 'Humberto', 'curso': 'Python'}
]


# CRUD
def adicionarAluno(nome: str, curso: str) -> None:
    mat = random.randint(3, 1000)
    aluno = {
        'matricula': mat,
        'nome': nome,
        'corso': curso
    }
    banco.append(aluno)
    print('Aluno cadastrado com sucesso!')


def listarAlunos() -> None:
    for aluno in banco:
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Curso: {aluno['curso']}")
        print("------------------------")


def buscarAlunos(matricula: int) -> None:
    existe = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Curso: {aluno['curso']}")
            print("------------------------")
            existe = True
    if not existe:
        print('Aluno não cadastrado!\n')


def editarAluno(matricula: int, novo_nome: str, novo_curso: str) -> None:
    existe = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            aluno['nome'] = novo_nome
            aluno['curso'] = novo_curso
            existe = True
            print('Dados alterados com sucesso!\n')
    if not existe:
        print('Aluno não cadastrado!\n')


def deletarAluno(matricula: int) -> None:
    existe = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            banco.remove(aluno)
            print('Dados alterados com sucesso!\n')
            existe = True
    if not existe:
        print('Aluno não encontrado!\n')


# MAIN

listarAlunos()

buscarAlunos(int(input(f'-- Buscar aluno\nMatrícula: ')))
editarAluno(int(input(f'--Editar aluno\nMatrícula: ')), input('Novo nome: '), input('Novo curso: '))
listarAlunos()
deletarAluno(int(input(f'--Deletar aluno\nMatrícula: ')))
listarAlunos()