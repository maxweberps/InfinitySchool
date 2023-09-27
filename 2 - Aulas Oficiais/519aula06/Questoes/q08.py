"""
3. Considere a seguinda lista = [5, 7, 9, 3, 2, 10, 15, 16],
escreva um algoritmo para obter o indice do item com o maior valor
"""

lista = [5, 7, 9, 20, 2, 10, 15, 16]

print(f'Lista: {lista}\n'
      f'O maior número é o {max(lista)}, indice {lista.index(max(lista))}\n'
      f'O menor número é {min(lista)}, indice {lista.index(min(lista))}')