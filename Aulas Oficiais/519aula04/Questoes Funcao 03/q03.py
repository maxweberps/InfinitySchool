"""
3. Escreva uma função que recebe três parametros, base maior, base menor e altura,
em seguida calcule a área do trapézio e exiba o resultado na tela
"""


def calcular_area(b_maior, b_menor, altura):
    area = (b_maior + b_menor) * altura / 2
    return area


print('--- Calcular área do Trapézio ---')
b_maior = float(input('Base maior (cm): '))
b_menor = float(input('Base menor (cm): '))
altura = float(input('Altura (cm): '))
print(f'Área: {calcular_area(b_maior, b_menor, altura)} cm²')
