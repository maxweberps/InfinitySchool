from operacoes import consulta, deposito, saque, transferencia
from banco import *


def menu():
    while True:
        print('---- BEM VINDO AO MENU ----')
        print('1 - Adicionar conta')
        print('2 - Editar nome')
        print('3 - Excluir conta')
        print('4 - Consultar conta')
        print('5 - Listar contas')
        print('6 - Consultar saldo')
        print('7 - Fazer depósito')
        print('8 - Fazer saque')
        print('9 - Transferência')
        print('10 - sair')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            nome = input('Digite o nome do cliente')
            saldo = float(input('Digite o saldo'))
            adicionar_conta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            novo_nome = input('Digite o novo nome: ')
        elif opcao == 3:
            conta = int(input('Digite o numero da conta: '))
            deletar_conta(conta)
        elif opcao == 4:
            conta = int(input('Digite o numero da conta: '))
            consultar_cliente(conta)
        elif opcao == 5:
            listar_contas()
        elif opcao == 6:
            conta = int(input('Digite o numero da conta: '))
            consulta.consultar_saldo()
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de deposito: '))
            deposito.depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de saque: '))
            saque.sacar(conta, valor)
        elif opcao == 9:
            contaOrigem = int(input('Digite o número da conta: '))
            contaDestino = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de transferencia: '))
            transferencia.transferir(contaOrigem, contaDestino, valor)
        elif opcao == 10:
            print('---- VOCÊ SAIU DO PROGRAMA ----')
            break


menu()
