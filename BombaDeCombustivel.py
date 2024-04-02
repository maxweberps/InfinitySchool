class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel

    def AbastecerPorValor(self, valor):
        litros = valor / self.valor_litro
        self.qtd_combustivel -= litros
        print(f'Quantidade abastecida: {litros:.2f} litros')
        print(f'Quantidade de combustível restante na bomba: {self.qtd_combustivel:.2f} litros')

    def AbastecerPorLitro(self, litro):
        self.qtd_combustivel -= litro
        print(f'Valor a ser pago: R$ {litro * self.valor_litro:.2f}')
        print(f'Quantidade de combustível restante na bomba: {self.qtd_combustivel:.2f} litros')

    def AlterarValor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f'Valor do litro alterado para: R$ {self.valor_litro}')

    def AlterarCombustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        print(f'Alterado tipo de combustível para {self.tipo_combustivel}')

    def AlterarQtdCombustivel(self, nova_qtd):
        self.qtd_combustivel = nova_qtd
        print(f'Quantidade do combustível da bomba alterada para {self.qtd_combustivel} litros')


print('================= Abastecimento =================')
print('> Montar bomba de combustível')
tipo = input('Tipo de combustível: ')
valor_litro = float(input('Valor do litro: R$ '))
qtd_combustivel = float(input('Quantidade de combustível na bomba (litro): '))

# instancia
bomba = BombaCombustivel(tipo, valor_litro, qtd_combustivel)

while (True):
    print('\n================== MENU ===================')
    op = input('1 - Abastecer (R$) \n'
               '2 - Abastecer (l)\n'
               '3 - Alterar valor do litro\n'
               '4 - Alterar tipo de combustível\n'
               '5 - Alterar quantidade de combustível na bomba\n'
               'Selecione uma opção: ')
    print('===========================================')

    if op == '1':
        bomba.AbastecerPorValor(float(input('Deseja abastecer quanto? (R$) ')))
    elif op == '2':
        bomba.AbastecerPorLitro(float(input('Deseja abastecer quanto? (l) ')))
    elif op == '3':
        bomba.AlterarValor(float(input('Novo preço do litro? (R$) ')))
    elif op == '4':
        bomba.AlterarCombustivel(input('Novo tipo de combustível: '))
    elif op == '5':
        bomba.AlterarQtdCombustivel(float(input('Nova quantidade de combustível na bomba? (l) ')))
    else:
        print('Opção inválida!')
