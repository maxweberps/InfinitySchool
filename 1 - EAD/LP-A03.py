'''
[LP-A03] Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
 O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
'''

num = int(input('Número: '))
for i in range(11, -10, -1):
    print(f'{num} x {i} = {num * i}')
