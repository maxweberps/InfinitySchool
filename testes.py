class Veiculo:

    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print("Veículo acelerando...")


class Carro(Veiculo):

    def acelerar(self):
        print("Carro acelerando...")


class Moto(Veiculo):

    def acelerar(self):
        print("Moto acelerando...")


def testar_aceleracao(veiculo):
    veiculo.acelerar()


veiculos = [Carro("Toyota"), Moto("Honda")]

for veiculo in veiculos:
    testar_aceleracao(veiculo)
