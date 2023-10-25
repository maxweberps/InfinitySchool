'''
[PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função
chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada
"verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7,
 "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
'''


def verificar_situacao(media):
    if media == 10:
        print('Parabéns, sua média é 10!')
    if media < 7:
        print('Reprovado.')
    elif media >= 7:
        print('Aprovado')


def calcular_media(notas):
    media = sum(notas) / len(notas)
    print(f'Média: {media:.2f}')
    verificar_situacao(media)


notas = []
i = 0
print('---- Lançar notas ----\n'
      'Para encerrar, digite -1')
while True:
    i += 1
    nota = float(input(f'Nota {i}: '))
    if nota == -1:
        break
    else:
        notas.append(nota)

calcular_media(notas)
