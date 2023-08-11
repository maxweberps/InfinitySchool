"""
2. Leia cinco itens adicione-os em uma lista.
Em seguida pergunta ao usuário qual item ele deseja remover, se o item existir na lista remova-o
"""
itens = []
for i in range(0, 5):
    itens.append(input('Digite um item: '))

print(f'Sua lista atual é: {itens}')

item = input('Qual item deseja remover da lista? ')

if item in itens:
    itens.remove(item)
    print(f'Item removido!\nLista atual: {itens}')
else:
    print('O objeto não existe na lista.')
