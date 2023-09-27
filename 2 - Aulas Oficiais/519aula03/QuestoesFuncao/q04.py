"""
4. Escreva uma função que leia dois números e imprima o maior
"""

def QualMaior():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    if num1 > num2:
        print(f'{num1} é maior que {num2}')
    else:
        print(f'{num2} é maior que {num1}')

QualMaior()