"""
1. Escreva uma função que recebe um parametro lado, em seguida calcule a área do quadrado e exiba o
resultado na tela area = lado * lado
"""

def calcular_area(lado):
    area = lado * lado
    print(f'Área: {area} cm²')

print('-- Calcular área do quadrado --')
lado = float(input('Lado (cm): '))
calcular_area(lado)
