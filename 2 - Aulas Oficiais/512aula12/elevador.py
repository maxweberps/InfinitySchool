'''
1. Crie uma classe chamada Elevador
Atributos:
-> andar atual(terreo = 0)
-> qtd andares
-> qtd pessoas : int
-> capacidade : int
Métodos
-> subir()
sobe +1 andar
[] não pode passar o ultimo andar
-> descer()
desce -1 andar
[] não pode passar do terreo
-> entrar(qtd)
-> sair(qtd)
'''


class Elevador:
    # Método construtor
    def __init__(self, andar_atual, qtd_pessoas,
                 qtd_andares, capacidade):
        self.andar_atual = andar_atual
        self.qtd_pessoas = qtd_pessoas
        self.qtd_andares = qtd_andares
        self.capacidade = capacidade

    # métodos
    def subir(self):
        if self.andar_atual < self.qtd_andares:
            self.andar_atual += 1
            print("Subindo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você está no ultimo andar!")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print("Descendo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você está no Térreo!")

    def entrar(self, qtd):
        if self.qtd_pessoas + qtd <= self.capacidade:
            self.qtd_pessoas += qtd
            print("Entrando...")
            print(f"Quantidade atual: {self.qtd_pessoas}")
        else:
            print("Capacidade não suporta essa quantidade!")

    def sair(self, qtd):
        self.qtd_pessoas -= qtd
        if self.qtd_pessoas < 0:
            self.qtd_pessoas = 0
        print("Saindo...")
        print(f"Quantidade atual: {self.qtd_pessoas}")


plaza = Elevador(5, 10, 7, 15)
plaza.subir()
plaza.subir()
plaza.subir()
plaza.entrar(5)
plaza.sair(15)
plaza.sair(2)
