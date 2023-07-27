"""
5. Escreva uma função que leia 3 notas, calcule a média e se a média for maior ou igual a 6 imprima "você esta aprovado" senão imprima "você está de recuperação"
"""

def Aprovacao():
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    media = (nota1+nota2+nota3)/3
    print(f'Sua média é {media:.2f}')
    if media >= 6:
        print('Você está aprovado!')
    else:
        print('Recuperação. Continue tentando!')


Aprovacao()