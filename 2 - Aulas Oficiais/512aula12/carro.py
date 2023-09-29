# Como criar uma classe
class Carro:

    # Método construtor: é o método executado quando o obj é criado
    def __init__(self, marca, modelo, ano):
        # atributos e métodos
        # atributos => caracteristicas
        # métodos => ações / comportamentos / funções
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = 0

    def acelerar(self, velocidade):
        self.velocidade_atual += velocidade
        print('VRRRRRRRRUMMM')
        print(f'Sua velocidade atual é {self.velocidade_atual} km/h')

    def exibirInformacoes(self):
        print('--- Informações do veículo ---')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')


print('--- Criação de carro')
print('> Crie seu carro:')
marca = input('Marca: ')
modelo = input('Modelo: ')
ano = input('Ano: ')
carro1 = Carro(marca, modelo, ano)
carro1.exibirInformacoes()
carro1.acelerar(10)
carro1.acelerar(10)
carro1.acelerar(10)
carro1.acelerar(100)