import fractions
from math import fabs
from struct import pack
from tkinter import *
import time
from turtle import width


master = Tk()
master.resizable(height = False, width = False)
master.title("Portal Investidor")
master.geometry("480x560+800+155")
master.iconbitmap(default="icones\\ico.ico")


def cadastrar():
    master.destroy()

    master1 = Tk()
    master1.title("Nova Janela criada!!")
    master1.geometry("490x560+400+153")


    lab2 = Label(master1, image=img_2)  
    lab2.grid()
# Variáveis globais
esconda_senha = StringVar()


# Importar imagens
img_1 = PhotoImage(file="imagens\\fundo.png")
img_2 = PhotoImage(file="imagens\\fundo2.png")
img_3 = PhotoImage(file="imagens\\bt-img.png")
img_4 = PhotoImage(file="imagens\\cadastro.png")
img_5 = PhotoImage(file="imagens\\cadastrar.png")

# Criação de labels
lab = Label(master, image=img_1)
lab.pack()




# Criação de caixas de entrada
email1 = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
email1.place(width=392, height=45, x=43, y=182)

senha1 = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
senha1.place(width=392, height=45, x=43, y=300)


# Criação de botões
entrar1 = Button(master, bd=0, image=img_3)
entrar1.place(width=118, height=64, x=270, y=408)

cadastro1 = Button(master, bd=0, image=img_4, command= cadastrar)
cadastro1.place(width=175, height=64, x=68, y=408)

master.mainloop()