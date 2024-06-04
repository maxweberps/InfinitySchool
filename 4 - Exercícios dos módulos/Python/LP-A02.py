"""
[LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h,
exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
"""

velocidade = float(input('Qual sua velocidade? '))
if velocidade > 80:
    valor_multa = (velocidade - 80) * 20
    print(f'Acima da velocidade permitida! Valor da multa: R${valor_multa}')
else:
    print('Dentro da velocidade permitida.')