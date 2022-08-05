from struct import pack
from tkinter import *
import time

master = Tk()
master.title("Portal Investidor")
master.geometry("490x560+800+153")
master.iconbitmap(default="icones\\ico.ico")
master.resizable(width=1, height=1)


# Funções
def Cadastro():
    master.destroy()
    time.sleep(0.3)

    master1 = Tk()
    master1.title("Cadastro !")
    master1.geometry("490x560+800+153")


def Tela_investimento():
    master.destroy()
    time.sleep(0.3)

    master1 = Tk()
    master1.title("tela de investimento !")
    master1.geometry("1200x500+400+153")    


# Variáveis globais
esconda_senha = StringVar()

# Importar imagens
img_fundo = PhotoImage(file="imagens\\fundo.png")
img_botao = PhotoImage(file="imagens\\bt-img.png")
img_botao2 = PhotoImage(file="imagens\\cadastro.png")

# Criação de labels
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()


# Criação de caixas de entrada
en_email = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_email.place(width=392, height=45, x=49, y=182)

en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
en_senha.place(width=392, height=45, x=49, y=300)


# Criação de botões
bt_entrar = Button(master, bd=0, image=img_botao,command=Tela_investimento)
bt_entrar.place(width=118, height=64, x=280, y=408)

bt_cadastro = Button(master, bd=0, image=img_botao2, command=Cadastro)
bt_cadastro.place(width=171, height=64, x=74, y=408)

master.mainloop()