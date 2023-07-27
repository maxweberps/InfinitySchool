qtd_par = 0
qtd_impar = 0

for i in range(0, 10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        qtd_par += 1
    else:
        qtd_impar += 1

print(f'{qtd_par} número são pares e {qtd_impar} são ímpares')
