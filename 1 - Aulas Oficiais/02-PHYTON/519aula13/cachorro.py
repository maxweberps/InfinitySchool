'''
Crie uma classe chamada Cachorro que possua 3 atributos: nome, raça e peso. Implemente um método:
comer ração, que retorna: "croc croc croc".
Crie duas instâncias dessa classe, e imprima na tela: "O cachorro nome_do_cachorro é da raça raça_do_cachorro,
pesa peso_do_cachorro quilos e come: croc croc croc".
'''


class Cachorro:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso

    def comer_racao(self):
        return 'croc, croc, croc..'


print('-- Crie seu cachorro')
cachorro01 = Cachorro(input('Nome: '),
                      input('Raça: '),
                      input('Peso: '))

print(f'O cachorro {cachorro01.nome}'
      f' é da raça {cachorro01.raca}'
      f' e pesa {cachorro01.peso} kg '
      f'e come {cachorro01.comer_racao()}')
