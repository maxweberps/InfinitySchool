"""
6. Escreva uma função que recebe um número por parametro e imprima uma sequencia de 0 até este número
"""


def castigo_do_bart(frase, qtd):
    for i in range(1, qtd + 1):
        print(f'{i}. {frase}')


print('--- Castigo do Bart ---')
frase = input('Digite uma frase: ')
qtd = int(input('Quantas vezes essa frase deve ser escrita na lousa? '))

castigo_do_bart(frase, qtd)
