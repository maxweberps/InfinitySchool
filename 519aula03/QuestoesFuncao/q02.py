"""
2. Escreva uma função que leia base e altura de um triangulo e imprima a sua área
area = base * altura / 2
"""

def AreaTriangulo():
    base = float(input('Valor da base: '))
    h = float(input('Valor da altura: '))
    print(f'A área do triangulo é {(base*h)/2}')


print('--- VAMOS CALCULAR A ÁREA DE UM TRIANGULOO ---')
AreaTriangulo()