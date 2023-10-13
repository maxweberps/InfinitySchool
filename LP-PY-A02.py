'''
[LP-PY-A02]Escreva um código em Python que peça três números e determine:
- O maior número;
- O menor número;
- Se existem números iguais e caso exista, quais são os números.
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
maior = n1
menor = n1

if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2

if n3 < menor:
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

if n1 == n2 == n3:
    print(f"Todos os números são iguais: {n1}")
elif n1 == n2:
    print(f"Os números iguais são: {n1} e {n2}")
elif n1 == n3:
    print(f"Os números iguais são: {n1} e {n3}")
elif n2 == n3:
    print(f"Os números iguais são: {n2} e {n3}")
else:
    print("Não existem números iguais.")

