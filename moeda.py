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



# Funções
#def Cadastro():
#    master.destroy()
#    time.sleep(0.3)
#
#    fr1.title("Cadastro !")
#    fr1.geometry("500x560+800+153") 
#
#
#def Tela_investimento():
#    master.destroy()
#    time.sleep(0.3)
#
#    fr2 = Tk()
#    fr2.title("tela de investimento !")
#    fr2.geometry("1200x500+400+153")  

   


# Variáveis globais
esconda_senha = StringVar()

# Importar imagens
img_fundo_fr0 = PhotoImage(file="imagens\\fundo.png")
img_fundo_fr1 = PhotoImage(file="imagens\\fundo2.png")
img_botao_fr0 = PhotoImage(file="imagens\\bt-img.png")
img_botao2_fr0 = PhotoImage(file="imagens\\cadastro.png")
img_botao3_fr1 = PhotoImage(file="imagens\\cadastrar.png")

# Criação de labels
lab_fundo_fr0 = Label(master, image=img_fundo_fr0).pack()

lab_fundo_fr1 = Label(master, image=img_fundo_fr1)


# Criação de caixas de entrada
en_email_fr0 = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_email_fr0.place(width=392, height=45, x=43, y=182)

en_senha_fro = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
en_senha_fro.place(width=392, height=45, x=43, y=300)


# Criação de botões
bt_entrar_fr0 = Button(master, bd=0, image=img_botao_fr0)
bt_entrar_fr0.place(width=120, height=64, x=270, y=408)

bt_cadastro_fr0 = Button(master, bd=0, image=img_botao2_fr0)
bt_cadastro_fr0.place(width=175, height=64, x=68, y=408)

master.mainloop()