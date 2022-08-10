from cProfile import label
from cgitb import text
from email.mime import image
from logging import root
from math import fabs
from struct import pack
from time import time
from tkinter import *


import tkinter as tk
from turtle import title, width

root = Tk()
root.title("Portal Investidor")
root.resizable(height = False, width = False)
root.geometry("484x560+800+155")
root.iconbitmap(default="icones\\ico.ico")


fr0 = Frame()
fr1 = Frame()
fr2 = Frame()
fr3 = Frame()
fr4 = Frame()
fr5 = Frame()


# Variáveis globais

def cpf(event=None):
    x=fr0_in2.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    fr0_in2.delete(0, 'end')
    fr0_in2.insert(0, y)

def cpf_1(event=None):
    x=fr1_in0.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    fr1_in0.delete(0, 'end')
    fr1_in0.insert(0, y)

def cnpj(event=None):
            x=fr0_in2.get().replace('.','').replace('/', '').replace('-', '')[:14]
            y=''
            if event.keysym.lower() == "backspace": return
            for i in range(len(x)):
                if x[i] in '01234567891011':
                    if i in [1,4]:
                        y+=x[i] + '.'
                    elif i == 7:
                        y+=x[i] + '/'
                    elif i == 11:
                        y+=x[i] + '-' 
                    else:
                        y+=x[i]
            fr0_in2.delete(0, 'end')
            fr0_in2.insert(0, y)


def cnpj_1(event=None):
            x=fr1_in0.get().replace('.','').replace('/', '').replace('-', '')[:14]
            y=''
            if event.keysym.lower() == "backspace": return
            for i in range(len(x)):
                if x[i] in '01234567891011':
                    if i in [1,4]:
                        y+=x[i] + '.'
                    elif i == 7:
                        y+=x[i] + '/'
                    elif i == 11:
                        y+=x[i] + '-' 
                    else:
                        y+=x[i]
            fr1_in0.delete(0, 'end')
            fr1_in0.insert(0, y)


hello = StringVar()
def mostrar(*args):
    fr0_in0 = Entry(fr0, textvariable=hello, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)
    feecho =  Button(fr0, image=fr0_img_3,bd=0, command=esconder).place(width=45, height=45, x=436, y=302)
    
def esconder(*args):
    fr0_in0 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)
    fr0_bt3 = Button(fr0, image=fr0_img_3,bd=0, command=mostrar).place(width=45, height=45, x=436, y=302)

hello_1 = StringVar()
def mostrar_1(*args):
    fr1_in1 = Entry(fr1, textvariable=hello_1, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=23, y=425)
    feecho = Button(fr1, bd=0, image=fr1_img_3, command=esconder_1).place(width=45, height=40, x=430, y=430)
    
def esconder_1(*args):
    fr1_in1 = Entry(fr1, textvariable=hello_1, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=23, y=425)
    fr1_bt3 = Button(fr1, bd=0, image=fr1_img_3, command=mostrar_1).place(width=45, height=40, x=430, y=430)


# Importar imagens

#frame 0
fr0_img_1 = PhotoImage(file="imagens\\fundo.png")
fr0_img_2 = PhotoImage(file="imagens\\entrar.png")
fr0_img_3 = PhotoImage(file="imagens\\olho.png")
fr0_img_4 = PhotoImage(file="imagens\\cadastro.png")

#frame 1
fr1_img_1 = PhotoImage(file="imagens\\cadastrar.png")
fr1_img_2 = PhotoImage(file="imagens\\fundo2.png")
fr1_img_3 = PhotoImage(file="imagens\\olho.png")
fr1_img_4 = PhotoImage(file="imagens\\voltar.png")
fr1_img_5 = PhotoImage(file="imagens\\olho.png")

#frame 2
fr2_img_1 = PhotoImage(file="imagens\\tela.png")
fr2_img_2 = PhotoImage(file="imagens\\guardar.png")
fr2_img_3 = PhotoImage(file="imagens\\comprar.png")
fr2_img_4 = PhotoImage(file="imagens\\vender.png")
fr2_img_5 = PhotoImage(file="imagens\\tabela.png")
fr2_img_6 = PhotoImage(file="imagens\\grafico.png")
fr2_img_7 = PhotoImage(file="imagens\\moedas.png")
fr2_img_8 = PhotoImage(file="imagens\\cotação do dia.png")
fr2_img_9 = PhotoImage(file="imagens\\media.png")
fr2_img_10 =  PhotoImage(file="imagens\\tela sem fundo.png")

#frame 3
fr3_img_1 = PhotoImage(file="imagens\\tela.png")
fr3_img_2 = PhotoImage(file="imagens\\guardar.png")
fr3_img_3 = PhotoImage(file="imagens\\comprar.png")
fr3_img_4 = PhotoImage(file="imagens\\vender.png")
fr3_img_5 = PhotoImage(file="imagens\\tabela.png")
fr3_img_6 = PhotoImage(file="imagens\\compra.png")
fr3_img_7 = PhotoImage(file="imagens\\comprar.png")
fr3_img_8 = PhotoImage(file="imagens\\limpa.png")
fr3_img_9 = PhotoImage(file="imagens\\confirmar.png")
fr3_img_10 = PhotoImage(file="imagens\\grafico.png")
fr3_img_11 = PhotoImage(file="imagens\\moedas.png")
fr3_img_12 = PhotoImage(file="imagens\\cotação do dia.png")
fr3_img_13 = PhotoImage(file="imagens\\media.png")

#frame 4
fr4_img_1 = PhotoImage(file="imagens\\tela.png")
fr4_img_2 = PhotoImage(file="imagens\\guardar.png")
fr4_img_3 = PhotoImage(file="imagens\\comprar.png")
fr4_img_4 = PhotoImage(file="imagens\\vender.png")
fr4_img_5 = PhotoImage(file="imagens\\tabela.png")
fr4_img_6= PhotoImage(file="imagens\\venda.png")
fr4_img_8 = PhotoImage(file="imagens\\limpa.png")
fr4_img_9 = PhotoImage(file="imagens\\confirmar.png")
fr4_img_10 = PhotoImage(file="imagens\\grafico.png")
fr4_img_11 = PhotoImage(file="imagens\\moedas.png")
fr4_img_12 = PhotoImage(file="imagens\\cotação do dia.png")
fr4_img_13 = PhotoImage(file="imagens\\media.png")

#frame 5
fr5_img_1 = PhotoImage(file="imagens\\tela.png")
fr5_img_2 = PhotoImage(file="imagens\\guardar.png")
fr5_img_3 = PhotoImage(file="imagens\\comprar.png")
fr5_img_4 = PhotoImage(file="imagens\\vender.png")
fr5_img_5 = PhotoImage(file="imagens\\tabela.png")
fr5_img_6= PhotoImage(file="imagens\\moeda e investir.png")
fr5_img_8 = PhotoImage(file="imagens\\limpa.png")
fr5_img_9 = PhotoImage(file="imagens\\confirmar.png")
fr5_img_10 = PhotoImage(file="imagens\\grafico.png")
fr5_img_11 = PhotoImage(file="imagens\\moedas.png")
fr5_img_12 = PhotoImage(file="imagens\\cotação do dia.png")
fr5_img_13 = PhotoImage(file="imagens\\media.png")

#frame 6


# Criação de labels 

#tela de fundo da tela de login

fr0_lab = Label(fr0, image=fr0_img_1,width=480).grid(row=0,column=0,sticky=W)


# Criação de caixas de entrada  

#frame 0 Tela de login

#entre do cpf e cnpj
fr0_in2 = Entry(fr0, bd=2, font=("Calibri", 15), justify=CENTER)
fr0_in2.place(width=392, height=45, x=37, y=185)
fr0_in2.bind('<KeyRelease>', cpf)
fr0_in2.bind('<KeyRelease>', cnpj)

#Entre da senha  
fr0_in3 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)

# Criação de botões 

# Botão do entrar
fr0_bt0 = Button(fr0, bd=0, image=fr0_img_2,command=lambda: [fr0.grid_remove(),fr2.grid(),root.geometry("1289x600+310+153")]).place(width=118, height=64, x=290, y=408)

# Botão do cadastro
fr0_bt2 = Button(fr0, bd=0, image=fr0_img_4 , command=lambda: [fr0.grid_remove(), fr1.grid()]).place(width=174, height=64, x=63, y=408)

# Botão do olho
fr0_bt3 = Button(fr0, bd=0, image=fr0_img_3, command=mostrar).place(width=45, height=45, x=436, y=302)


# Frame 1 Tela de Cadastro

# Criação de labels 

#tela de fundo do Cadastro
fr1_lab2 = Label(fr1, image=fr1_img_2,width=480).grid(row=0,column=0) 

# Criação de caixas de entrada 

#entre do cpf e cnpj
fr1_in0 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER)
fr1_in0.place(width=392, height=45, x=20, y=130)
fr1_in0.bind('<KeyRelease>', cpf_1)
fr1_in0.bind('<KeyRelease>', cnpj_1)

#Entre da senha  
fr1_in1 = Entry(fr1, textvariable=hello_1, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=23, y=425)


#Entre do Nome
fr1_in2 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=20, y=202)

#Entre do Data de Nascimento
fr1_in3 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=22, y=273)

#Entre do telefone
fr1_in4 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=22, y=343)

# Criação de botões 


# Botão do Cadastrar
fr1_bt0 = Button(fr1, bd=0, image=fr1_img_1, command=lambda: [fr1.grid_remove(), fr0.grid()]).place(width=173, height=64, x=243, y=488) #Cadastrar

# Botão do olho
fr1_bt3 = Button(fr1, bd=0, image=fr1_img_3, command=mostrar_1).place(width=45, height=40, x=430, y=430) #Olho

# Botão do Voltar
fr1_bt2 = Button(fr1, bd=0, image=fr1_img_4 , command=lambda: [fr1.grid_remove(), fr0.grid()]).place(width=170, height=58, x=35, y=490) #Voltar


# frame 2 Tela do investidor

# Criação de labels 

fr2_lab = Label(fr2, image=fr2_img_1, width=1285).grid(row=0,column=0,sticky=W)

fr2_lab1 = Label(fr2,bd=0, image=fr2_img_5).place(width=305, height=65, x=974, y=26)

fr2_lab2 = Label(fr2, image=fr2_img_6, width=1000).place(width=950, height=470, x=5, y=125) # grafico

fr2_lab3 = Label(fr2,bd=0, image=fr2_img_7).place(width=178, height=52, x=30, y=148) # label moeda

fr2_lab4 = Label(fr2,bd=0, image=fr2_img_8).place(width=218, height=52, x=222, y=148) # label cotação

fr2_lab5 = Label(fr2,bd=0, image=fr2_img_9).place(width=480, height=52, x=462, y=148) # label media

fr2_lab6 = Label(fr2, image=fr2_img_10,bd=0).place(width=310, height=470, x=970, y=130)
# Criação de botões

# Botão de guardar
fr2_bt1 = Button(fr2, bd=0, image=fr2_img_2, command= lambda:[fr2.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=675, y=32)
# Botão de comprar
fr2_bt2 = Button(fr2, bd=0, image=fr2_img_3, command= lambda:[fr2.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de vender
fr2_bt3 = Button(fr2, bd=0, image=fr2_img_4, command= lambda:[fr2.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=367, y=32)



# frame 3 # tela da Compra

# Criação de labels 


# tela do Investidor de Compra
fr3_lab = Label(fr3, image=fr3_img_1, width=1285).grid(row=0,column=0,sticky=W)

# imahem compra
fr3_lab1 = Label(fr3, image=fr3_img_6,bd=0).place(width=310, height=470, x=970, y=130)

# image tabela
fr3_lab2 = Label(fr3,bd=0, image=fr3_img_5).place(width=305, height=65, x=974, y=26)
#tela do grafico
fr3_lab3 = Label(fr3, image=fr3_img_10, width=1000).place(width=950, height=470, x=5, y=125) # 


fr3_lab4 = Label(fr3,bd=0, image=fr3_img_11).place(width=178, height=52, x=30, y=148) # label moeda

fr3_lab5 = Label(fr3,bd=0, image=fr3_img_12).place(width=218, height=52, x=222, y=148) # label cotação

fr3_lab6 = Label(fr3,bd=0, image=fr3_img_13).place(width=480, height=52, x=462, y=148) # label media

fr3_lab7 = Label(fr3, text='ola', font=("Calibri", 15)).place(width=145, height=24, x=995, y=400) #Montante

# Criação de botões 

# Botão de guardar
fr3_bt1 = Button(fr3, bd=0, image=fr3_img_2, command= lambda:[fr3.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=675, y=32)
# Botão de comprar
fr3_bt2 = Button(fr3, bd=0, image=fr3_img_3, command= lambda:[fr3.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de vender
fr3_bt3 = Button(fr3, bd=0, image=fr3_img_4, command= lambda:[fr3.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=367, y=32)
# Botão de limpar
fr3_bt4 = Button(fr3, bd=0, image=fr3_img_8).place(width=115, height=42, x=996, y=503)
#  botão de Confirmar
fr3_bt5 = Button(fr3, bd=0, image=fr3_img_9).place(width=115, height=42, x=1137, y=504)



fr3_in1 = Entry(fr3, bd=2, font=("Calibri", 15)).place(width=140, height=24, x=995, y=200) #moeda
fr3_in2 = Entry(fr3, bd=2, font=("Calibri", 15)).place(width=140, height=24, x=995, y=265) #capital
fr3_in4 = Entry(fr3, bd=2, font=("Calibri", 15)).place(width=145, height=24, x=995, y=325) #Tempo



# frame 4 # tela da Venda

# Criação de labels 

# tela do Investidor de Compra
fr4_lab = Label(fr4, image=fr4_img_1, width=1285).grid(row=0,column=0,sticky=W)

# imahem compra
fr4_lab1 = Label(fr4,bd=0, image=fr4_img_6).place(width=310, height=470, x=970, y=130)

# image tabela
fr4_lab2 = Label(fr4,bd=0, image=fr4_img_5).place(width=305, height=65, x=974, y=26)

#tela do grafico
fr4_lab3 = Label(fr4, image=fr4_img_10, width=1000).place(width=950, height=470, x=5, y=125) #

fr4_lab4 = Label(fr4,bd=0, image=fr4_img_11).place(width=178, height=52, x=30, y=148) # label moeda

fr4_lab5 = Label(fr4,bd=0, image=fr4_img_12).place(width=218, height=52, x=222, y=148) # label cotação

fr4_lab6 = Label(fr4,bd=0, image=fr4_img_13).place(width=480, height=52, x=462, y=148) # label media

fr4_lab7 = Label(fr4,text='ola', font=("Calibri", 15)).place(width=145, height=24, x=993, y=454) #Montante

# Criação de botões 

# Botão de guardar
fr4_bt1 = Button(fr4, bd=0, image=fr4_img_2, command= lambda:[fr4.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=675, y=32)
# Botão de comprar
fr4_bt2 = Button(fr4, bd=0, image=fr4_img_3, command= lambda:[fr4.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de vender
fr4_bt3 = Button(fr4, bd=0, image=fr4_img_4, command= lambda:[fr4.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=367, y=32)

# Botão de limpar
fr4_bt4 = Button(fr4, bd=0, image=fr4_img_8).place(width=115, height=42, x=996, y=504)
#  botão de Confirmar
fr4_bt5 = Button(fr4, bd=0, image=fr4_img_9).place(width=115, height=42, x=1137, y=504)


fr4_in1 = Entry(fr4, bd=2, font=("Calibri", 15)).place(width=140, height=24, x=993, y=222) #moeda a vender
fr4_in2 = Entry(fr4, bd=2, font=("Calibri", 15)).place(width=140, height=24, x=993, y=287) #capital
fr4_in3 = Entry(fr4, bd=2, font=("Calibri", 15)).place(width=145, height=24, x=993, y=390) #moeda a comprar

# frame 5 Tela de Guardar

# Criação de labels 

# tela do Investidor de Guardar
fr5_lab = Label(fr5, image=fr5_img_1, width=1285).grid(row=0,column=0,sticky=W) # imagem de fundo

# imagem do moeda e investir
fr5_lab1 = Label(fr5,bd=0, image=fr5_img_6).place(width=310, height=470, x=970, y=130)

# imagem Tabela 
fr5_lab2 = Label(fr5,bd=0, image=fr5_img_5).place(width=305, height=65, x=974, y=26)

#tela do grafico
fr5_lab3 = Label(fr5, image=fr5_img_10, width=1000).place(width=950, height=470, x=5, y=125) #

fr5_lab4 = Label(fr5,bd=0, image=fr5_img_11).place(width=178, height=52, x=30, y=148) # label moeda

fr5_lab5 = Label(fr5,bd=0, image=fr5_img_12).place(width=218, height=52, x=222, y=148) # label cotação

fr5_lab6 = Label(fr5,bd=0, image=fr5_img_13).place(width=480, height=52, x=462, y=148) # label media

fr5_lab7 = Label(fr5,text= 'ola', font=("Calibri", 15)).place(width=145, height=24, x=991, y=416) #Montante

# Criação de botões 

# Botão de guardar
fr5_bt1 = Button(fr5, bd=0, image=fr5_img_2, command= lambda:[fr5.grid_remove(),fr5.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=675, y=32)
# Botão de compra
fr5_bt2 = Button(fr5, bd=0, image=fr5_img_3,command= lambda:[fr5.grid_remove(),fr3.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=54, y=32)
# Botão de venda
fr5_bt3 = Button(fr5, bd=0, image=fr5_img_4,command= lambda:[fr5.grid_remove(),fr4.grid(),root.geometry("1289x600+310+153")]).place(width=223, height=60, x=367, y=32)
# Botão de limpar
fr5_bt4 = Button(fr5, bd=0, image=fr5_img_8).place(width=115, height=42, x=996, y=510)
#  botão de Confirmar
fr5_bt5 = Button(fr5, bd=0, image=fr5_img_9).place(width=115, height=42, x=1130, y=510)



fr5_in1 = Entry(fr5, bd=2, font=("Calibri", 15)).place(width=140, height=24, x=992, y=222) #moeda a Inserir
fr5_in2 = Entry(fr5, bd=2, font=("Calibri", 15)).place(width=140, height=24, x=992, y=287) #capital
fr5_in3 = Entry(fr5, bd=2, font=("Calibri", 15)).place(width=145, height=24, x=990, y=348) #Tempo



fr0.grid()
root.mainloop()