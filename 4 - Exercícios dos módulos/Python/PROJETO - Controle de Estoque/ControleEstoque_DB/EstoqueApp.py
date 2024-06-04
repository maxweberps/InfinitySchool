from EstoqueData import *
from Venda import *


class EstoqueApp:
    def __init__(self):
        self.db = EstoqueData()

        while True:
            print('\n--- MENU ESTOQUE ---')
            print('Selecione uma opção: ')
            op = input(f'1 - Cadastrar produto\n'
                       f'2 - Listar produtos\n'
                       f'3 - Atualizar produto\n'
                       f'4 - Lançar venda\n'
                       f'5 - REL: Faturamento por período\n'
                       f'6 - REL: Faturamento por produto\n'
                       f'7 - Sair\n'
                       f'R: ')
            if op == '1':
                self.cadastrar_produto()
            elif op == '2':
                self.listar_produtos()
            elif op == '3':
                self.atualizar_produto()
            elif op == '4':
                self.lancar_venda()
            elif op == '5':
                self.gerar_rel_periodo()
            elif op == '6':
                self.gerar_rel_produto()
            elif op == '7':
                break
            else:
                print('Opção inválida. Tente novamente.')

    def cadastrar_produto(self):
        print('\n> Cadastro de produto')
        nome = input('Nome: ')
        descricao = input('Descrição: ')
        preco = float(input('Preço: R$ '))
        qtd_disp = input('Quantidade inicial: ')
        produto = Produto(nome, descricao, preco, qtd_disp)
        self.db.inserir_produto(produto)

    def listar_produtos(self):
        print('\n##### Lista de produtos no estoque #####')
        print('COD.....NOME.....DESCRIÇÃO.....PRECO.....QTD DISP')
        produtos = self.db.listar_produtos()
        for p in produtos:
            print(f'{p["id_prod"]}.....{p["nome"]}.....{p["descricao"]}.....R$ {p["preco"]:.2f}.....{p["qtd_disp"]}')

    def exibir_produto(self, id_prod):

        if self.db.consultar_produto(id_prod):
            p = self.db.consultar_produto(id_prod)

            # exibe produto selecionado
            print('\n> Produto selecionado: ')
            print(f'Nome: {p.nome}\n'
                  f'Descrição: {p.descricao}\n'
                  f'Preço: R$ {p.preco:.2f}\n'
                  f'Quantidade disponível: {p.qtd_disp}')
            return True

        else:
            print('Produto não encontrado.')
            return False

    def atualizar_produto(self):

        # selecionar o produto
        print('\n> Selecionar produto')
        id_prod = int(input('ID: '))

        # testa se o produto existe e exibe seus dados
        if self.exibir_produto(id_prod):
            # atualiza dados
            print('\n> Atualizar produto: ')
            nome = input('Novo nome: ')
            descricao = input('Nova descrição: ')
            preco = float(input('Novo preço: R$ '))
            qtd_disp = float(input('Nova quantidade disponível: '))
            novo_prod = Produto(nome, descricao, preco, qtd_disp)
            novo_prod.id_prod = id_prod
            self.db.atualizar_produto(novo_prod)

    def lancar_venda(self):
        # selecionar o produto
        print('\n> Selecionar produto')
        id_prod = int(input('ID: '))

        # testa se o produto existe e exibe seus dados
        if self.exibir_produto(id_prod):
            # montar venda
            print('\n >Lançar venda ')
            qtd = float(input('Quantidade vendida: '))
            data = input('Data da venda (AAAA-MM-DD): ')
            venda = Venda(id_prod, qtd, data)
            self.db.inserir_venda(venda)

            # deduz qtd do produto no estoque
            p = self.db.consultar_produto(id_prod)
            p.qtd_disp -= qtd
            self.db.atualizar_produto(p)

    def gerar_rel_periodo(self):
        print('\n> Relatório de faturamento por período')
        data_ini = input('\nData início (AAAA-MM-DD): ')
        data_fim = input('Data fim (AAAA-MM-DD): ')
        vendas = self.db.consultar_por_periodo(data_ini, data_fim)
        print('\nID VENDA.....DATA.....PRODUTO.....PREÇO UN.....QTD.....SUB-TOTAL')
        total = 0
        sub_total = 0
        for venda in vendas:
            sub_total = self.db.consultar_produto(venda["id_prod"]).preco * venda["qtd"]
            total += sub_total
            print(f'{venda["id_venda"]}.....{venda["data_venda"]}.....'
                  f'{self.db.consultar_produto(venda["id_prod"]).nome}.....'
                  f'{self.db.consultar_produto(venda["id_prod"]).preco:.2f}.....'
                  f'{venda["qtd"]}.....'
                  f'{sub_total:.2f}')

        print(f'\nTotal: R$ {total:.2f}')

    def gerar_rel_produto(self):
        print('\n> Relatório de faturamento por produto')
        print('\n> Selecionar produto')
        id_prod = int(input('ID: '))
        if self.exibir_produto(id_prod):
            vendas = self.db.consultar_por_produto(id_prod)
            print('\nID VENDA.....DATA.....PRODUTO.....PREÇO UN.....QTD.....SUB-TOTAL')
            total = 0
            sub_total = 0
            qtd_saida = 0
            for venda in vendas:
                sub_total = self.db.consultar_produto(venda["id_prod"]).preco * venda["qtd"]
                total += sub_total
                qtd_saida += venda["qtd"]
                print(f'{venda["id_venda"]}.....{venda["data_venda"]}.....'
                      f'{self.db.consultar_produto(venda["id_prod"]).nome}.....'
                      f'{self.db.consultar_produto(venda["id_prod"]).preco:.2f}.....'
                      f'{venda["qtd"]}.....'
                      f'{sub_total:.2f}')

            print(f'\nQuantidade saída: {qtd_saida}'
                  f'\nTotal: R$ {total:.2f}')


if __name__ == "__main__":
    app = EstoqueApp()
