class Elevador:
    # Método construtor
    def __init__(self, atualAndar, atualCapacidade,
                 totalAndar, totalCapacidade):
        self.atualAndar = atualAndar
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.totalCapacidade = totalCapacidade

    # métodos
    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print("Subindo...")
            print(f"Andar atual: {self.atualAndar}")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print("Descendo...")
            print(f"Andar atual: {self.atualAndar}")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa.")
            print(f"Quantidade atual: {self.atualCapacidade}")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def sair(self):
        if self.atualCapacidade > 0:
            print('Saindo uma pessoa.')
            self.atualCapacidade -= 1
            print(f"Quantidade atual: {self.atualCapacidade}")
        else:
            print("NÃO TEM NINGUÉM")


# criando cenário
print('> Criar cenário ')
total_andares = int(input('Total de andares: '))
andar_atual = int(input('Andar atual: '))
total_capacidade = int(input('Capacidade total do elevador: '))
qtd_atual = int(input('Quantidade atual de pessoas no elevador: '))

# instanciando objeto
plaza = Elevador(andar_atual, qtd_atual, total_andares, total_capacidade)

while(True):
    print('=============================')
    op = input('1 - Subir\n'
               '2 - Descer\n'
               '3 - Entrar\n'
               '4 - Sair\n'
               'Selecione uma opção: ')
    print('=============================')

    if op == '1':
        plaza.subir()
    elif op == '2':
        plaza.descer()
    elif op == '3':
        plaza.entrar()
    elif op == '4':
        plaza.sair()
    else:
        print('Opção inválida!')