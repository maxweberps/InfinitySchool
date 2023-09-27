"""
1. Crie uma lista com 3 notas (coloque os valores que quiser),
em seguida acessando os itens, calcule a média dessas notas e exiba na tela
"""
notas = [10,5.6,8.2]


print(notas)
media = sum(notas) / len(notas)
print(f'Média = {media:.2f}')

"""
2. Acesse a segunda nota da lista e altere o seu valor para 9.99
notas[1] = 9.99
"""

notas[1] = 9.99
print(notas)
media = sum(notas) / len(notas)
print(f'Média = {media:.2f}')