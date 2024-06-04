import pymysql.cursors
from Produto import *
from Venda import *


class EstoqueData:
    def __init__(self):
        # cria conexão com o banco
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='estoque',
                                       cursorclass=pymysql.cursors.DictCursor)
        # cria cursor
        self.cursor = self.conexao.cursor()

    def inserir_produto(self, p: Produto):
        try:
            sql = 'INSERT INTO produtos (nome, descricao, qtd_disp, preco) values (%s,%s,%s,%s)'
            self.cursor.execute(sql, (p.nome, p.descricao, p.qtd_disp, p.preco))
            self.conexao.commit()
            print('> Produto cadastrado com sucesso.')
        except Exception as error:
            print(f'Erro ao inserir! Erro: {error}')

    def listar_produtos(self):
        try:
            sql = 'SELECT * FROM produtos'
            self.cursor.execute(sql)
            produtos = self.cursor.fetchall()
            return produtos
        except Exception as error:
            print(f'Erro ao listar! Erro: {error}')

    def consultar_produto(self, id_prod):
        try:
            sql = 'SELECT * FROM produtos WHERE id_prod = %s'
            self.cursor.execute(sql, id_prod)
            p_dict = self.cursor.fetchone()
            p = Produto(p_dict["nome"], p_dict["descricao"], p_dict["preco"], p_dict["qtd_disp"])
            p.id_prod = p_dict["id_prod"]
            return p
        except Exception as error:
            print(f'Erro ao listar! Erro: {error}')
            return False

    def atualizar_produto(self, p: Produto):
        try:
            sql = 'UPDATE produtos SET nome = %s, descricao = %s, qtd_disp = %s,' \
                  'preco = %s WHERE id_prod = %s'
            self.cursor.execute(sql, (p.nome,
                                      p.descricao,
                                      p.qtd_disp,
                                      p.preco,
                                      p.id_prod))
            self.conexao.commit()
            print('\n> Dados atualizados com sucesso.')
        except Exception as error:
            print(f'Erro ao atualizar! Erro: {error}')

    def inserir_venda(self, v: Venda):
        try:
            sql = 'INSERT INTO vendas (id_prod, qtd, data_venda) values (%s,%s,%s)'
            self.cursor.execute(sql, (v.id_prod, v.qtd, v.data))
            self.conexao.commit()
            print('\n> Venda lançada com sucesso.')
        except Exception as error:
            print(f'Erro ao inserir! Erro: {error}')

    def consultar_por_periodo(self, data_ini, data_fim):
        try:
            sql = 'SELECT * FROM vendas WHERE data_venda BETWEEN %s AND %s ORDER BY data_venda DESC'
            self.cursor.execute(sql, (data_ini, data_fim))
            vendas = self.cursor.fetchall()
            return vendas
        except Exception as error:
            print(f'Erro ao buscar relatório! Erro: {error}')
            return False

    def consultar_por_produto(self, id_prod):
        try:
            sql = 'SELECT * FROM vendas WHERE id_prod = %s ORDER BY data_venda DESC'
            self.cursor.execute(sql, id_prod)
            vendas = self.cursor.fetchall()
            return vendas
        except Exception as error:
            print(f'Erro ao buscar relatório! Erro: {error}')
            return False
