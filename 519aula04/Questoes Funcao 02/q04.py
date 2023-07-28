"""
4. Escreva uma função que recebe um número por parametro e informe se ele este parametro é par ou ímpar
"""

def par_ou_impar(num):
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')

print('--- Par ou impar? ---')
num = int(input('Número: '))
par_ou_impar(num)