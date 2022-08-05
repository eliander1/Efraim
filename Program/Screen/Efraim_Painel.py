from tkinter import *
from Program.Buttons.Botao import Atualizar

# INTERFACE

janela = Tk()
janela.title("Painel Efraim")

texto_orientacao = Label(janela, text='Clique para atualizar o painel')
texto_orientacao.grid(column=0, row=0, padx=50, pady=10)


botao = Button(janela, text='Atualizar painel', command=Atualizar, bg="green", fg="white")
botao.grid(column=0, row=1, padx=50, pady=10)


# sempre colocar isso no final pra manter a janela aberta
janela.mainloop()