lista_de_compras = []


def add_produto():
    print('\n> Adicionar produto\n--')
    nome = input('Nome: ')
    qtd = int(input('Quantidade: '))
    v_unit = float(input('Valor unitário: R$'))
    v_total = qtd * v_unit
    produto = {'nome': nome, 'qtd': qtd, 'v_unit': v_unit, 'v_total': v_total}
    return produto


def ver_lista():
    print('\n> Lista de produtos')
    print('NOME.....QTD.....UNIT....TOTAL')
    for produto in lista_de_compras:
        print(f'{produto["nome"]}.....{produto["qtd"]}.....{produto["v_unit"]:.2f}.....{produto["v_total"]:.2f}')
    print(f'> Total: R$ {valor_total():.2f}')


def atualizar_produto():
    print('\n> Atualizar produto\n--')
    nome = input('Nome do produto: ')
    achou = False
    for indice, produto in enumerate(lista_de_compras):
        if nome == produto['nome']:
            lista_de_compras[indice]['nome'] = input('Novo nome: ')
            lista_de_compras[indice]['qtd'] = int(input('Nova quantidade: '))
            lista_de_compras[indice]['v_unit'] = float(input('Novo valor unitário: R$'))
            lista_de_compras[indice]['v_total'] = lista_de_compras[indice]['qtd'] * lista_de_compras[indice]['v_unit']
            achou = True
    if achou:
        print('Produto atualizado com sucesso.')
    else:
        print('Produto não localizado.')


def valor_total():
    v_total = 0
    for produto in lista_de_compras:
        v_total += produto['v_total']
    return v_total


def remover_produto():
    print('\n> Remover produto\n--')
    nome = input('Nome do produto: ')
    achou = False
    for indice, produto in enumerate(lista_de_compras):
        if nome == produto['nome']:
            del lista_de_compras[indice]
            print(f'O produto {produto["nome"]} foi removido com sucesso.')
            achou = True
    if achou:
        pass
    else:
        print('Produto não localizado.')


while True:
    print('\n--- Lista de Produtos ---')
    print('Selecione uma opção: ')
    op = input(f'1 - Adicionar produto\n'
               f'2 - Remover produto\n'
               f'3 - Atualizar produto\n'
               f'4 - Ver lista de produtos\n'
               f'5 - Encerrar programa\n'
               f'R: ')
    if op == '5':
        print('\nFim.')
        break
    elif op == '1':
        lista_de_compras.append(add_produto())
    elif op == '2':
        remover_produto()
    elif op == '3':
        atualizar_produto()
    elif op == '4':
        ver_lista()
    else:
        print('Opção inválida. Tente novamente.')
