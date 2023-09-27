from banco import obter_conta, banco


def depositar(conta: int, valor: float) -> None:
    cliente = obter_conta(conta)
    if cliente:
        cliente['saldo'] = cliente['saldo'] + valor
        print('Depósito realizado com sucesso!')
    else:
        print('Cliente não existe!')


if __name__ == '__main__':
    depositar(1, 100)
    print(banco)
