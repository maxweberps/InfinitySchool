"""
1. Número perfeito:
O número perfeito é resultado da soma de todos os seus divisores menos ele proprio
Ex: 6 é um número perfeito pois a soma de seus divisores (1, 2, 3) é igual a 6.
Escreva uma função que recebe um número e informe se ele é ou não um número perfeito
"""


def teste_perfeito(num):
    cont = 0
    for i in range(1, num):
        if num % i == 0:
            cont += i

    if cont == num:
        return True
    else:
        return False


print('--- Teste de número perfeito ---')
if teste_perfeito(int(input('Qual número deseja testar? '))):
    print('É perfeito')
else:
    print('Não é perfeito')
