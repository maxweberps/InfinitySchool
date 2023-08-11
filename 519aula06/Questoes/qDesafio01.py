"""
Considere a seguinte lista = [5, 7, 9, 3, 2, 10, 15, 16]. Utilize for para imprimir ao final do programa a
quantidade de números primos contidos na lista. número primo => só é divisivel por 1 e ele mesmo.
"""

lista = [5, 7, 9, 3, 2, 10, 15, 16]


for num in lista:
    qtd_divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            qtd_divisores += 1
    if qtd_divisores == 2:
        print(f'O numero {num} é primo')
