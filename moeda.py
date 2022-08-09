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
    fr1_in1 = Entry(fr1, textvariable=hello_1, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=30, y=245)
    feecho = Button(fr1, bd=0, image=fr1_img_3, command=esconder_1).place(width=45, height=40, x=430, y=248) #Olho
    
def esconder_1(*args):
    fr1_in1 = Entry(fr1, textvariable=hello_1, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=30, y=245)
    fr1_bt3 = Button(fr1, bd=0, image=fr1_img_3, command=mostrar_1).place(width=45, height=40, x=430, y=248) #Olho

hello_2 = StringVar()
def mostrar_2(*args):
    fr1_in2 = Entry(fr1, textvariable=hello_2, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=30, y=338)
    feecho =  Button(fr1, bd=0, image=fr1_img_5, command=esconder_2).place(width=45, height=40, x=430, y=343) #Olho
    
def esconder_2(*args):
    fr1_in2 = Entry(fr1, textvariable=hello_2, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=30, y=338)
    fr1_bt4 = Button(fr1, bd=0, image=fr1_img_5, command=mostrar_2).place(width=45, height=40, x=430, y=343) #Olho

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

#frame 3
#fr3_img_1= PhotoImage(file="imagens\\compra.png")
#fr3_img_2= PhotoImage(file="imagens\\venda.png")
fr3_img_3= PhotoImage(file="imagens\\moeda e investir.png")

# Criação de labels 

fr0_lab = Label(fr0, image=fr0_img_1,width=480).grid(row=0,column=0,sticky=W)


# Criação de caixas de entrada  

#frame 0

fr0_in2 = Entry(fr0, bd=2, font=("Calibri", 15), justify=CENTER)
fr0_in2.place(width=392, height=45, x=37, y=185)
fr0_in2.bind('<KeyRelease>', cpf)
fr0_in2.bind('<KeyRelease>', cnpj)

fr0_in3 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)

# Criação de botões 

fr0_bt0 = Button(fr0, bd=0, image=fr0_img_2,command=lambda: [fr0.grid_remove(),fr2.grid(),root.geometry("1289x600+310+153")]).place(width=118, height=64, x=290, y=408)


fr0_bt2 = Button(fr0, bd=0, image=fr0_img_4 , command=lambda: [fr0.grid_remove(), fr1.grid()]).place(width=174, height=64, x=63, y=408)

fr0_bt3 = Button(fr0, bd=0, image=fr0_img_3, command=mostrar).place(width=45, height=45, x=436, y=302)


# Frame 1

# Criação de labels 

fr1_lab2 = Label(fr1, image=fr1_img_2,width=480).grid(row=0,column=0) 

# Criação de caixas de entrada 

fr1_in0 = Entry(fr1, bd=2, font=("Calibri", 15), justify=CENTER)
fr1_in0.place(width=392, height=45, x=30, y=152)
fr1_in0.bind('<KeyRelease>', cpf_1)
fr1_in0.bind('<KeyRelease>', cnpj_1)

fr1_in1 = Entry(fr1, textvariable=hello_1, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=30, y=245)

fr1_in2 = Entry(fr1, textvariable=hello_2, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=30, y=338)

# Criação de botões 


fr1_bt0 = Button(fr1, bd=0, image=fr1_img_1, command=lambda: [fr1.grid_remove(), fr0.grid()]).place(width=173, height=64, x=243, y=430) #Cadastrar

fr1_bt3 = Button(fr1, bd=0, image=fr1_img_3, command=mostrar_1).place(width=45, height=40, x=430, y=248) #Olho

fr1_bt2 = Button(fr1, bd=0, image=fr1_img_4 , command=lambda: [fr1.grid_remove(), fr0.grid()]).place(width=170, height=58, x=35, y=433) #Voltar

fr1_bt4 = Button(fr1, bd=0, image=fr1_img_5, command=mostrar_2).place(width=45, height=40, x=430, y=343) #Olho


# Criação de labels 

fr2_lab = Label(fr2, image=fr2_img_1, width=1285).grid(row=0,column=0,sticky=W)
fr2_lab1 = Label(fr2,bd=0, image=fr2_img_5).place(width=305, height=65, x=974, y=26)
#width=305, height=65, x=974, y=26

# Criação de botões 

fr2_bt1 = Button(fr2, bd=0, image=fr2_img_2,command= lambda:[fr3.place()]).place(width=223, height=60, x=675, y=32)
fr2_bt2 = Button(fr2, bd=0, image=fr2_img_3).place(width=223, height=60, x=54, y=32)
fr2_bt3 = Button(fr2, bd=0, image=fr2_img_4).place(width=223, height=60, x=367, y=32)


# frame 3
# Criação de labels 
fr3_lab = Label(fr3,bd=0, image=fr3_img_3).place(width=310, height=470, x=970, y=130)

fr0.grid()
root.mainloop()