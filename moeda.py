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



# Variáveis globais
esconda_senha = StringVar()


# Importar imagens
img1 = PhotoImage(file="imagens\\fundo.png")
img2 = PhotoImage(file="imagens\\fundo2.png")
img3 = PhotoImage(file="imagens\\bt-img.png")
img4 = PhotoImage(file="imagens\\cadastro.png")
img5 = PhotoImage(file="imagens\\cadastrar.png")

# Criação de labels
lab1 = Label(master, image=img1)
lab1.place(x=0, y=0)

#lab2 = Label(master, image=img2)
#lab2.place(x=0, y=0)


# Criação de caixas de entrada
email1 = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
email1.place(width=392, height=45, x=43, y=182)

senha1 = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
senha1.place(width=392, height=45, x=43, y=300)


# Criação de botões
entrar1 = Button(master, bd=0, image=img1)
entrar1.place(width=120, height=64, x=270, y=408)

cadastro1 = Button(master, bd=0, image=img2, command= lambda: [fr0.place_forget(), fr1.place(x=0, y=0)])
cadastro1.place(width=175, height=64, x=68, y=408)

master.mainloop()