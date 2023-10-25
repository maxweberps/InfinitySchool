'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
Função filter() para obter uma nova lista com números pares da lista numeros
Função reduce() para obter a soma de todos os números da lista numeros
'''
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def quadrado(num):
    return num ** 2


num_quadrado = map(quadrado, numeros)
print(list(num_quadrado))

num_pares = filter(lambda num: num % 2 == 0, numeros)
print(list(num_pares))

num_soma = reduce(lambda x, y: x + y, numeros)
print(num_soma)
