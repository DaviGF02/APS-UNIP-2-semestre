# Software para Criptografia de Mensagens

# Importando bibliotecas e Módulos

from functools import partial
from tkinter import *
from Funcoes import *

# Propriedades da Janela

janela = Tk()
janela.geometry("800x600+250+30")
janela.title("Auto Cripto")
janela.resizable(width=False, height=False)
janela.configure(background="#836FFF")

# Widgets

titulo = Label(janela, text="Auto Cripto", width=20, height=2, font=("Arial", 30), background="#836FFF")
titulo.place(x=170, y=10)

lb1 = Label(janela, text="Insira a Mensagem para ser Criptografada/Descriptograda:", background="#FFDAB9")
lb1.place(x=40, y=130)

lb2 = Label(janela, text="A Mensagem de saída será exibida aqui:", background="#FFDAB9")
lb2.place(x=490, y=130)

txt1 = Text(janela, width=45, height=20)
txt1.place(x=20, y=160)

txt2 = Text(janela, width=45, height=20)
txt2.place(x=420, y=160)

# Funções e Botões

CriptoPy = Funções(txt1, txt2)

btn1 = Button(janela, width=20, text="Criptografar", command=CriptoPy.cript, background="#FFDAB9")
btn1.place(x=30, y=500)

btn2 = Button(janela, width=20, text="Descriptografar", command=CriptoPy.descript, background="#FFDAB9")
btn2.place(x=220, y=500)

btn3 = Button(janela, width=20, text="Copiar Mensagem", command=CriptoPy.areaTransf, background="#FFDAB9")
btn3.place(x=430, y=500)

btn4 = Button(janela, width=20, text="Salvar Mensagem", command=CriptoPy.salvaTexto, background="#FFDAB9")
btn4.place(x=620, y=500)

janela.mainloop()

