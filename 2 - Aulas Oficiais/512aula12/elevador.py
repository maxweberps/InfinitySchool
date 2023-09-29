class Elevador:
    def __init__(self, qtd_andares):
        self.andar_atual = 0
        self.qtd_andares = qtd_andares


    def subir(self):
        if self.andar_atual < self.qtd_andares:
            self.andar_atual += 1
            print(f'Subindo... Andar atual: {self.andar_atual}')
        else:
            print('Já está no andar máximo.')
