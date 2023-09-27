"""
2. Escreva uma função que recebe dois parametros, base e altura, em seguida calcule a
área do triangulo e exiba o resultado na tela
"""


def calcular_area(base, altura):
    area = base * altura / 2
    print(f'Área: {area} cm²')


print('--- Calcular área do Triângulo ---')
base = float(input('Base (cm): '))
altura = float(input('Altura (cm): '))
calcular_area(base, altura)
