"""
1. Crie duas listas vazias uma chamada "pares" e outra chamada "impares", em seguida leia 10 números (utilize for),
se o número for par, adicione-o na lista de pares, se o número for ímpar adicione-o na lista de ímpares
"""

pares = []
impares = []

for i in range(0,10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Numeros pares: {pares}\n'
      f'Numeros impares: {impares}')