'''
[LP-PY-A03]Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba:

- A média de idade de todo o grupo.

- Qual o nome da pessoa mais velha.

- Quantas pessoas têm menos de 20 anos.

- Quantas pessoas têm mais de 40 anos.

- Qual o sexo da pessoa mais nova.
'''

nome = []
idade = []
sexo = []

for i in range(1, 4):
    print(f'-- Pessoa {i}')
    nome.append(input('Nome: '))
    idade.append(int(input('Idade: ')))
    sexo.append(input('Sexo: '))

print(f'A média de idade das pessoas é {sum(idade) / len(idade)}')
print(f'A pessoa mais velha é {nome[idade.index(max(idade))]}, com {max(idade)} anos')

cont20menos = 0
cont40mais = 0
for i in idade:
    if i < 20:
        cont20menos += 1
    if i > 40:
        cont40mais += 1

print(f'Existem {cont20menos} pessoas com idade menor que 20 anos')
print(f'Existem {cont40mais} pessoas com idade maior que 40 anos')
print(f'O sexo da pessoa mais nova é {sexo[idade.index(min(idade))]},'
      f'com {min(idade)} anos e se chama {nome[idade.index(min(idade))]}')
