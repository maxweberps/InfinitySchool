import pymysql.cursors

'''
connection
cursor
'''

# Como criar uma conexão

try:
    conexao = pymysql.connect(host='localhost', user='root',
                              password='', db='escola',
                              cursorclass=pymysql.cursors.DictCursor)
    print('Conexão estabelecida com sucesso!')
except Exception as erro:
    print(f'Erro ao conectar banco! Erro: {erro}')

# Criando um cursor
cursor = conexao.cursor()


def consultar():
    try:
        sql = 'select * from alunos'
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(f'Nome: {aluno["nome"]}, Curso: {aluno["curso"]}')
    except Exception as erro:
        print(f'Erro ao lista os alunos! Erro: {erro}')


def inserir(nome, idade, curso, nota):
    try:
        sql = 'INSERT INTO alunos (nome, idade, curso, nota) values' \
              '(%s,%s,%s,%s)'
        cursor.execute(sql, (nome, idade, curso, nota))
        conexao.commit()
        print('Aluno matriculado com sucesso')
    except Exception as error:
        print(f'Erro ao cadastrar! Erro: {error}')


def aluno_existe(id):
    # Consulta se o aluno com o id existe
    sql = 'Select * from alunos where id = %s'
    cursor.execute(sql, id)
    resultado = cursor.fetchall()
    if resultado:
        return True
    else:
        return False


def editar(nome, idade, curso, nota, id):
    try:

        if aluno_existe(id):
            # update
            sql = 'Update alunos set nome = %s, idade = %s, curso = %s,' \
                  'nota = %s where id = %s'
            cursor.execute(sql, (nome, idade, curso, nota, id))
            conexao.commit()
            print('Dados alterados com sucesso!')
        else:
            print('Id não encontrado')
    except Exception as error:
        print(f'Erro ao atualizar! Erro: {error}')


def deletar(id):
    try:
        if aluno_existe(id):
            sql = 'Delete from alunos where id = %s'
            cursor.execute(sql, id)
            conexao.commit()
            print('Aluno removido com sucesso!')
        else:
            print('Id não encontrado!')
    except Exception as error:
        print('')


# inserir('Max Weber', 25, 'Java', 10)
# editar('Marcelo', 29, 'Python', 8, 10)
deletar(3)
consultar()
