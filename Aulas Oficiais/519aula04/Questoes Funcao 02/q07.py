"""
7. Escreva uma função que recebe um número por parametro e imprima todos os números pares de 0 até este número
"""


def num_pares(num):
    for i in range(0, num+1):
        if i % 2 == 0:
            print(i)

print('--- Númeres pares ---')
num = int(input('Deseja testar até que número? '))
print(f'Estes são os números pares até {num}:')
num_pares(num)
