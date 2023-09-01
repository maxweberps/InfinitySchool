
banco = [
    {'conta': 1, 'nome': 'Mariana', 'saldo': 159.99},
    {'conta': 2, 'nome': 'Jonas', 'saldo': 205.50}

]

conta_atual = 2


def adicionar_conta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    cliente = {
        'conta': conta_atual,
        'nome': nome,
        'saldo': saldo
    }
    banco.append(cliente)
    print('Cliente cadastrado com sucesso!')


def obter_conta(conta: int) -> dict or None:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
        return None


def deletar_conta(conta: int) -> None:
    cliente = obter_conta(conta)
    if cliente:
        banco.remove(cliente)
        print('Cliente deletado com sucesso!')
    else:
        print('Cliente não existe!')


def editar_nome(novo_nome: str, conta: int) -> None:
    cliente = obter_conta(conta)
    if cliente:
        cliente['nome'] = novo_nome
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não existe!')


def consultar_cliente(conta: int) -> None:
    cliente = obter_conta(conta)
    if cliente:
        print(f'N. Conta: {conta}\n'
              f'Cliente: {cliente["nome"]}\n'
              f'Saldo: {cliente["saldo"]}')
    else:
        print('Cliente não existe')


def listar_contas() -> None:
    for cliente in banco:
        consultar_cliente(cliente['conta'])
        print('-------------------------')


if __name__ == '__main__':
    adicionar_conta('Lucas', 950)
    editar_nome('Lucas Sousa', 3)
    print(banco)
