import random


class Conta:
    def __init__(self, numero, nome_cliente, saldo):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.saldo = saldo

    def exibir_dados(self):
        print(f'-- DADOS DA CONTA\n'
              f'Numero: {self.numero}\n'
              f'Nome {self.nome_cliente}\n'
              f'Saldo: {self.saldo}')

    def consultar_saldo(self):
        print(f'Seu saldo atual é: R$ {self.saldo}\n')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            c.consultar_saldo()
        else:
            print('Valor inválido. Digite um valor maior que 0!\n')


class ContaCorrente(Conta):
    def __init__(self, numero, nome_cliente, saldo, cheque_especial):
        super().__init__(numero, nome_cliente, saldo)
        self.cheque_especial = 1000

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Cheque especial: R$ {self.cheque_especial}')


class ContaPoupanca(Conta):
    def __init__(self, numero, nome_cliente, saldo, tx_rendimento):
        super().__init__(numero, nome_cliente, saldo)
        self.tx_rendimento = '1% a.a'

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Taxa de rendimento: {self.tx_rendimento}')


print('>> Cadastro de C/C')
c = ContaCorrente(random.randint(1000, 9999),
                  input('Nome do cliente: '),
                  input('Saldo inicial: R$ '), 0)
c.exibir_dados()

print('>> Cadastro de Poupança')
p = ContaPoupanca(random.randint(1000, 9999),
                  input('Nome do cliente: '),
                  input('Saldo inicial: R$ '), 0)
p.exibir_dados()
