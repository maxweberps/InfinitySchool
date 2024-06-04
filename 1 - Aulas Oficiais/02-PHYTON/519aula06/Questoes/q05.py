
numeros = [10,16,18,19,17,15,12,20,22,100]

maior,menor = numeros[0],numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'O maior número é {maior}\n'
      f'O menor número é {menor}')