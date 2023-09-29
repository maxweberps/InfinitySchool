palavra = 'kayak'
nova_palavra = ''

for i in range(len(palavra) - 1, -1, -1):
    nova_palavra += (palavra[i])

print(palavra)
print(nova_palavra)

if palavra == nova_palavra:
    print('é pali')
else:
    print('não é pali')
