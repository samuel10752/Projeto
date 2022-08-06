
from email.mime import image
from logging import root
from math import fabs
from struct import pack
from tkinter import *

import tkinter as tk
from turtle import width

root = Tk()
root.title("Portal Investidor")
#root.resizable(height = False, width = False)
root.geometry("484x560+800+155")
root.iconbitmap(default="icones\\ico.ico")


fr0 = Frame()
fr1 = Frame()

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



hello = StringVar()
def mostrar(*args):
    fr0_in0 = Entry(fr0, textvariable=hello, bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)

    feecho =  Button(fr0, text='👁', font=('Mongolian Baiti', "30", "bold"),bg='blue',fg='#fff', command=esconder).place(width=45, height=45, x=436, y=302)
    
def esconder(*args):
    fr0_in0 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)

    fr0_bt3 = Button(fr0, text='👁', font=('Mongolian Baiti', "30", "bold"),bg='blue',fg='#fff', command=mostrar).place(width=45, height=45, x=436, y=302)


# Importar imagens

fr0_img_1 = PhotoImage(file="imagens\\fundo.png")
fr1_img_2 = PhotoImage(file="imagens\\fundo2.png")
fr0_img_3 = PhotoImage(file="imagens\\bt-img.png")
fr0_img_4 = PhotoImage(file="imagens\\cadastro.png")
fr1_img_5 = PhotoImage(file="imagens\\cadastrar.png")

# Criação de labels 

fro_lab = Label(fr0, image=fr0_img_1,width=480).grid(row=0,column=0,sticky=W)

# Criação de caixas de entrada  

#frame 0

fr0_in2 = Entry(fr0, bd=2, font=("Calibri", 15), justify=CENTER)
fr0_in2.place(width=392, height=45, x=37, y=185)
fr0_in2.bind('<KeyRelease>', cpf)
fr0_in2.bind('<KeyRelease>', cnpj)

fr0_in3 = Entry(fr0, textvariable=hello, show="*", bd=2, font=("Calibri", 15), justify=CENTER).place(width=392, height=45, x=37, y=302)

# Criação de botões 

fr0_bt0 = Button(fr0, bd=0, image=fr0_img_3).place(width=118, height=64, x=290, y=408)

fr0_bt2 = Button(fr0, bd=0, image=fr0_img_4 , command=lambda: [fr0.grid_remove(), fr1.grid()]).place(width=174, height=64, x=63, y=408)

fr0_bt3 = Button(fr0, text='👁', font=('Mongolian Baiti', "30", "bold"),bg='blue',fg='#fff', command=mostrar).place(width=45, height=45, x=436, y=302)


# Frame 1

# Criação de labels 

fr1_lab2 = Label(fr1, image=fr1_img_2).grid(row=0,column=0) 

# Criação de caixas de entrada 


# Criação de botões 


fr0.grid()
root.mainloop()