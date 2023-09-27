"""
2. Escreva uma função que recebe dois parametros, base e altura, em seguida calcule a
área do triangulo e exiba o resultado na tela
"""


def calcular_area(base, altura):
    area = base * altura / 2
    return area


print('--- Calcular área do Triângulo ---')
base = float(input('Base (cm): '))
altura = float(input('Altura (cm): '))
print(f'Área: {calcular_area(base, altura)} cm²')
