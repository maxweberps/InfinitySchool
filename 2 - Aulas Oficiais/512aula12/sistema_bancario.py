import random


class Conta:
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.limite = 500
        self.extrato = []
        print('Conta criada com sucesso!\n')

    def consultarConta(self):
        print(f'> Dados da conta: \n'
              f'Número: {self.numero}\n'
              f'Nome do cliente: {self.nome}\n'
              f'Saldo: R$ {self.saldo}\n'
              f'Limite (cheque-especial): R$ {self.limite}\n')

    def consultarSaldo(self):
        print(f'Seu saldo atual é: R$ {self.saldo}\n')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(valor)
            conta.consultarSaldo()
        else:
            print('Valor inválido. Digite um valor maior que 0!\n')

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.extrato.append(valor * -1)
            conta.consultarSaldo()
        elif valor <= 0:
            print('Valor inválido. Valor menor que 0!\n')
        elif valor > self.saldo:
            print('Saldo insuficiente!\n')
            conta.consultarSaldo()

    def consultarExtrato(self):
        print(f'> Seu extrato')
        for i in conta.extrato:
            if i > 0:
                print(f'Depósito: R$ {i}')
            else:
                print(f'Saque: R$ {i}')
        conta.consultarSaldo()


print('-- Criar conta --')
nome = input('Nome do cliente: ')
saldo = float(input('Saldo inicial: '))
numero = random.randint(1000, 9999)

conta = Conta(numero, nome, saldo)
conta.consultarConta()

while True:
    op = input('--- MENU ---\n'
               '1 - Sacar\n'
               '2 - Depositar\n'
               '3 - Consultar extrato\n'
               '4 - Visualizar dados da conta\n'
               '5 - Sair\n'
               'R: ')

    if op == '5':
        break
    elif op == '1':
        saq_valor = float(input('\nValor do saque: '))
        conta.sacar(saq_valor)
    elif op == '2':
        dep_valor = float(input('\nValor do depósito: '))
        conta.depositar(dep_valor)
    elif op == '3':
        conta.consultarExtrato()
    elif op == '4':
        conta.consultarConta()
