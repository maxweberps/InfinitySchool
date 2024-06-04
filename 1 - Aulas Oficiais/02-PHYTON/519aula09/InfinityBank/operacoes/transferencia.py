from banco import obter_conta, banco


def transferir(conta_ori: int, conta_dest: int, valor: float) -> None:
    print(conta_ori)
    print(conta_dest)
    conta_origem = obter_conta(conta_ori)
    conta_destino = obter_conta(conta_dest)

    print(conta_origem)
    print(conta_destino)

    if conta_origem and conta_destino:
        if conta_origem['saldo'] >= valor:
            conta_origem['saldo'] -= valor
            conta_destino['saldo'] += valor
            print('Transferecia realizado com sucesso')
        else:
            print('Saldo insuficiente')
    else:
        print('Uma ou mais contas não existem!')


if __name__ == "__main__":
    print(banco)
    transferir(1, 2, 10)
    print(banco)
