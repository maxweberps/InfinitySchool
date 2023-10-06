import random


class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f'Matrícula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Salário: {self.salario}')


class Professor(Funcionario):
    def __init__(self, matricula, nome, salario, turma):
        super().__init__(matricula, nome, salario)
        self.turma = turma

    def exibir_dados(self):
        print('\nDados do Professor: ')
        super().exibir_dados()
        print(f'Turma: {self.turma}\n')


class Monitor(Funcionario):
    def __init__(self, matricula, nome, salario, ch):
        super().__init__(matricula, nome, salario)
        self.ch = ch

    def exibir_dados(self):
        print('\nDados do Monitor: ')
        super().exibir_dados()
        print(f'Carga horária: {self.ch}\n')


class Coordenador(Funcionario):
    def __init__(self, matricula, nome, salario, area):
        super().__init__(matricula, nome, salario)
        self.area = area

    def exibir_dados(self):
        print('\nDados do Coordenador: ')
        super().exibir_dados()
        print(f'Área: {self.area}\n')


print('-- Cadastro de funcionário.')

print('>> Professor')
p = Professor(random.randint(1111, 9999),
              input('Nome: '),
              input('Salário: '),
              input('Turma: '))
p.exibir_dados()

print('>> Monitor')
m = Monitor(random.randint(1111, 9999),
            input('Nome: '),
            input('Salário: '),
            input('CH: '))
m.exibir_dados()

print('>> Coordenador')
c = Coordenador(random.randint(1111, 9999),
                input('Nome: '),
                input('Salário: '),
                input('Área: '))
c.exibir_dados()
