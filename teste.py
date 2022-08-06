from tkinter import *

#criar janela

root = Tk()
root.title("密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密")


bg = PhotoImage(file = "fundo.png") 
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0) 


root.geometry("700x1000")
root.minsize(700, 1000) 
root.maxsize(700, 1000)
#geometria



#criar os widgets
bt = PhotoImage(file = "bt.png") 


bt1 = Button(root,bg='red' ,image=bt, activebackground="red")
bt2 = Button(root, text='Bt2')
bt3 = Button(root, text='Bt3')
bt4 = Button(root, text='Bt4')

bt1 = Button(root, text='Novo Sorteio')
bt2 = Button(root, text='Ver Sorteio')
bt3 = Button(root, text='Cadastrar Participantes')
bt4 = Button(root, text='Finalizar Sorteio')



#organizar os widgets

bt1.place(x= 180, y= 450)
bt2.place(x= 280, y= 450)
bt3.place(x= 180, y= 550)
bt4.place(x= 180, y= 650)

#executar a janela
root.mainloop()