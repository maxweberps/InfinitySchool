from tkinter import *
# Caixas de mensagem
from tkinter import messagebox


def enviar() -> None:
    num_serie = txt_nome.get()
    messagebox.showinfo('Sucesso!', f'Coletor de série {num_serie} cadastrado!')
    # Apagar texto do campo
    txt_nome.delete(0, END)


# Como criar uma janela
janela = Tk()

# Como alterar o tamanho da janela
janela.geometry("350x300")

# Como alterar o titulo da janela
janela.title("Magalu - Gestão de Equipamentos WMS")

# Como criar um label
label_nome = Label(janela, text='Num. Série: '
                   , foreground='black',
                   font='Tohoma 10')

# Adicionando o componente com grid
label_nome.grid(row=0, column=0)

# Como criar uma caixa de texto?
txt_nome = Entry(janela, font='Tohoma 10',
                 width=15)
txt_nome.grid(row=0, column=1)

# Como criar um botão
btn_enviar = Button(janela, text='Enviar',
                    background='black',
                    foreground='white',
                    font='Tohoma 10',
                    width=8,
                    command=enviar)
btn_enviar.grid(row=1, column=0, columnspan=2)

# Função que mantem a janela no S.O.
janela.mainloop()
