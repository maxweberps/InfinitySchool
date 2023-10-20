from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from aluno import Aluno


class App:
    def __init__(self):
        self.alunos = []
        self.janela = Tk()
        self.janela.title('SysAlunos')
        # LABEL
        # MATRICULA
        self.label_matricula = Label(self.janela, text='Matricula',
                                     font='Tahoma 14 bold', fg='red')
        self.label_matricula.grid(row=0, column=0)
        # NOME
        self.label_nome = Label(self.janela, text='Nome',
                                font='Tahoma 14 bold', fg='red')
        self.label_nome.grid(row=1, column=0)
        # IDADE
        self.label_idade = Label(self.janela, text='Idade',
                                 font='Tahoma 14 bold', fg='red')
        self.label_idade.grid(row=2, column=0)
        # CURSO
        self.label_curso = Label(self.janela, text='Curso',
                                 font='Tahoma 14 bold', fg='red')
        self.label_curso.grid(row=3, column=0)
        # NOTA
        self.label_nota = Label(self.janela, text='Nota',
                                font='Tahoma 14 bold', fg='red')
        self.label_nota.grid(row=4, column=0)

        # CAIXAS DE TEXTO
        # MATRICULA
        self.txt_matricula = Entry(self.janela, font='Tahoma 14',
                                   width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1)
        # NOME
        self.txt_nome = Entry(self.janela, font='Tahoma 14',
                              width=27)
        self.txt_nome.grid(row=1, column=1)
        # IDADE
        self.txt_idade = Entry(self.janela, font='Tahoma 14',
                               width=27)
        self.txt_idade.grid(row=2, column=1)
        # CURSO - COMBO BOX
        self.cursos = ['Python', 'JavaScript', 'DJango', 'ReactJs']
        self.cb_cursos = ttk.Combobox(self.janela, values=self.cursos, width=28,
                                      font='Tahoma 12')
        self.cb_cursos.grid(row=3, column=1)
        # NOTA
        self.txt_nota = Entry(self.janela, font='Tahoma 14',
                              width=27)
        self.txt_nota.grid(row=4, column=1)

        # BOTÕES
        # ADICIONAR
        self.botao_adicionar = Button(self.janela, font='Tahoma 12 bold', width=7,
                                      text='Adicionar', fg='red', command=self.adicionarAluno)
        self.botao_adicionar.grid(row=5, column=0)
        # EDITAR
        self.botao_editar = Button(self.janela, font='Tahoma 12 bold', width=7,
                                   text='Editar', fg='red')
        self.botao_editar.grid(row=5, column=1)
        # DELETAR
        self.botao_deletar = Button(self.janela, font='Tahoma 12 bold', width=7,
                                    text='Deletar', fg='red')
        self.botao_deletar.grid(row=5, column=2)

        # FRAME
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)

        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
        self.tabela.pack()
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)

        # SOBE A JANELA
        self.janela.mainloop()

    def adicionarAluno(self) -> None:
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.cb_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        self.alunos.append(aluno)
        messagebox.showinfo("Sucesso!", "Aluno adicionado com sucesso!")
        print(self.alunos)
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.txt_nota.delete(0, END)
        self.cb_cursos.set('')
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)

    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for aluno in self.alunos:
            self.tabela.insert('', END, values=(aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))

    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        item = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, item[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, str(item[1]))
        self.txt_idade.insert(0, str(item[2]))
        self.cb_cursos.set(item[3])
        self.txt_nota.insert(0, str(item[4]))


if __name__ == '__main__':
    app = App()
