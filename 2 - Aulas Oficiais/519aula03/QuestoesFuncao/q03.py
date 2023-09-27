"""
3. Escreva uma função que leia peso e altura de uma pessoa a imprima o seu IMC
imc = peso / altura ** 2
"""


def Imc():
    peso = float(input('Qual seu peso? (KG) '))
    h = float(input('Qual sua altura? (M) '))
    print(f'Seu IMC é {peso / (h ** 2):.2f}')


print('--- VAMOS CALCULAR SEU IMC ---')
Imc()
