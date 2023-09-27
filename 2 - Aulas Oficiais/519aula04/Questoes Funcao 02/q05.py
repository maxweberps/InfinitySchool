"""
5. Escreva uma função que recebe dois números por parametro e imprima o maior
"""


def qual_maior(n1, n2):
    if n1 > n2:
        print(f'{n1} é maior que {n2}')
    else:
        print(f'{n2} é maior que {n1}')


print('--- Qual número é maior? ---')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
qual_maior(n1, n2)
