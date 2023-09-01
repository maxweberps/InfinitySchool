from banco import obter_conta, banco


def consultar_saldo(conta: int) -> None:
    cliente = obter_conta(conta)
    if cliente:
        print(f'Saldo: {cliente["saldo"]}')
    else:
        print('Conta não existe')


if __name__ == '__main__':
    consultar_saldo(1)
    print(banco)
