'''
[LP-A04] Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o
usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
'''

cont = 0
num = 0
soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    else:
        cont += 1
        soma += num

print(f'Foram digitados {cont} números\n'
      f'A some deles é {soma} \n'
      f'A média é {soma/cont}')
