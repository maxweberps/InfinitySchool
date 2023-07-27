"""
7. Escreva uma função que leia 10 números e imprima a quantidade de pares, impares e números maiores que 20
"""


def Minhafuncao():
    qtd_par, qtd_impar, qtd_maiorquevinte = 0,0,0
    for i in range(0, 10):
        num = int(input('Digite um número: '))
        if num % 2 == 0:
            qtd_par += 1
        else:
            qtd_impar += 1
        if num > 20:
            print(f'{num} é maior que 20!')
            qtd_maiorquevinte += 1
    print(f'{qtd_par} número são pares, {qtd_impar} são ímpares e {qtd_maiorquevinte} números são maiores que 20')


Minhafuncao()
