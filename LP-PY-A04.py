'''
[LP-PY-A04]Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência
até que ele acerte. Para ajudar o usuário, o programa deve informar se o número é maior ou menor que o número a ser
adivinhado. Ao final, imprima o número adivinhado e a quantidade de tentativas.
'''

num = 10
tentativas = 0

while True:
    tentativas += 1
    palpite = int(input('Tente adivinha o número: '))
    if palpite == num:
        print(f'Parabéns, você acertou!! \nTentativas: {tentativas}')
        break
    else:
        if num > palpite:
            print('Tente um número maior')
        else:
            print('Tente um número menor')
        print('Não foi dessa vez. Continue tentando...')