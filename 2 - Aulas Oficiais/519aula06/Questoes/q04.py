"""
2. Considere a seguinte lista de números = [10, 16, 18, 19, 17, 15, 12, 20, 22],
utilize for para percorrer esta lista e imprima apenas os números pares, senão imprima "este número é ímpar
 e informe a quantidade de numeros pares e impares ao final
"""

numeros = [10, 16, 18, 19, 17, 15, 12, 20, 22]
qtd_par, qtd_impar = 0,0

for num in numeros:
    if num % 2 == 0:
        print(f'{num} é par')
        qtd_par += 1
    else:
        print(f'{num} é impar')
        qtd_impar += 1

print(f'\nExistem {qtd_par} números pares e {qtd_impar} numeros impares')
