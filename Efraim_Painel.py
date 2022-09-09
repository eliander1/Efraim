from tkinter import *
from Screen.Botao import Atualizar
from efraimbot.efraimbot.bot import Bot
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode='w')

logger = logging.getLogger(__name__)
logger.info('abrindo interface...')

# INTERFACE

janela = Tk()
janela.title("Painel Efraim")

texto_orientacao = Label(janela, text='Clique para atualizar o painel')
texto_orientacao.grid(column=0, row=0, padx=50, pady=10)


botao = Button(janela, text='Atualizar Painel', command=Atualizar, bg="green", fg="white")
botao.grid(column=0, row=1, padx=50, pady=10)

Ligar = Button(janela, text='Ligar o Painel', command=Bot.main, bg="blue", fg="white")
Ligar.grid(column=0, row=2, padx=50, pady=10)

# sempre colocar isso no final pra manter a janela aberta
janela.mainloop()