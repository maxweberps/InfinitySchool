# DICIONÁRIOS

fiado = {
    'jonas': 55.50,
    'marina': 15.00,
    'luana': 105.90,
    'matheus': 500.00
}

print(f'Quanto o Jonas deve? R$ {fiado["jonas"]}')

# para adicionar nova chave
fiado["joana"] = float(input('Valor que a Joana deve: '))
print(fiado)


# adicionar novo cliente
cliente = input('Nome do cliente: ')
fiado[cliente] = float(input('Valor: '))
print(fiado)

# navegar no dicionário
for chave in fiado:
    print(f'Cliente: {chave}\n'
          f'Dívida: {fiado[chave]}')

# remover elementos
del fiado['max']
print(fiado)

# visualizar todas as chaves
print(fiado.keys())

# vusualizar todas os valores
print(fiado.items())