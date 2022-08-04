from cProfile import label
from cgitb import text
from sqlite3 import Row
from tkinter import *
from tkinter import font
from turtle import color

#modelo de Janela	

root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
#root.overrideredirect(True)
root.geometry('300x300+820+300') # declara o tamanho
root.config(background='#D8D8D8') #background color
fr1 = LabelFrame(bg='#409FDE',pady=5)

#letras #(#409FDE) azul
#front  #(#1D7334)

#widgets
lb1_fr1 = Label(fr1, text='Tesouro Direto',foreground='#1CF00E', font='20',background='#409FDE').grid(row=0, column=1, sticky=W,padx=95)

#---Configuração do Frame---
fr1.grid()

# Executar
root.mainloop()