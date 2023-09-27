"""
print(len("Infinity School"))

if "a" in "banana":
    print("Tem a letra a")
else:
    print('Não tem a letra A')

1. Considere a seguinte lista de produtos = ["mouse", "teclado", "fone", "gabinete", "monitor"],
escreva um algoritmo para imprimir o produto com o maior nome da lista.
"""

produtos = ["mouse", "teclado", "fone", "gabinete", "monitorrrrr"]
maior_item = produtos[0]
for i in produtos:
   if len(i) > len(maior_item):
       maior_item = i

print(f'o item com mais caracteres é o {maior_item}')