from logging import root
from tkinter import *


root = Tk()
root.title("Tela do investidor")
root.geometry("1289x600+310+153")
#root.resizable(height = False, width = False)
root.iconbitmap(default="icones\\ico.ico")


fr2 = Frame()
fr3 = Frame()

#frame 2
fr2_img_1 = PhotoImage(file="imagens\\tela.png")
fr2_img_2 = PhotoImage(file="imagens\\guardar.png")
fr2_img_3 = PhotoImage(file="imagens\\comprar.png")
fr2_img_4 = PhotoImage(file="imagens\\vender.png")
fr2_img_5 = PhotoImage(file="imagens\\tabela.png")

#frame 3
fr2_img_6= PhotoImage(file="imagens\\compra.png")

# Criação de labels 

fr2_lab = Label(fr2, image=fr2_img_1, width=1285).grid(row=0,column=0,sticky=W)
fr2_lab1 = Label(fr2,bd=0, image=fr2_img_5).place(width=305, height=65, x=974, y=26)

# Criação de botões 

fr2_bt1 = Button(fr2, bd=0, image=fr2_img_2).place(width=223, height=60, x=675, y=32)
fr2_bt2 = Button(fr2, bd=0, image=fr2_img_3).place(width=223, height=60, x=54, y=32)
fr2_bt3 = Button(fr2, bd=0, image=fr2_img_4).place(width=223, height=60, x=367, y=32)


# frame 3
# Criação de labels 

fr2_lab2 = Label(fr2,bd=0, image=fr2_img_6).place(width=310, height=470, x=970, y=130)


fr2.grid()
root.mainloop()