"""
Escreva um algoritmo, que leia um número e informe se ele é ou não um número perfeito
"""

num = int(input('Digite um número: '))

for j in range(1, num + 1):
    cont = 0
    for i in range(1, j):
        if j % i == 0:
            cont += i

    if cont == j:
        print(f'{j} é perfeito')
    else:
        print(f'{j} não é perfeito')
