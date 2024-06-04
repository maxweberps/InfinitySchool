'''
Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar
os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a
quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
'''

valores = []
pares = []
impares = []

for i in range(1, 6):
    valores.append(int(input(f'Valor {i}: ')))

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

t_valores = (pares, impares)

print(f'Números pares e impares: {t_valores}')
print(f'Quantidade de números pares: {len(pares)}')
print(f'Quantidade de números impares: {len(impares)}')
print(f'Soma dos números pares: {sum(pares)}')
print(f'Soma dos números impares: {sum(impares)}')