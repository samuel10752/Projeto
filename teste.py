
from tkinter import *
import time

#Tela de Login
#===============================================================
jpas = Tk()
jpas.title("Cadastro de senha")

def bt_oksenha():
    p1=str(passwd.get())
    lb["text"] =str("A senha digitada foi {}".format(p1))


def bt_entrar(passw1=None):
    p1=str(passwd.get())
    p2=str(confpas.get())
    if p1 == p2:
        lb["text"] = str("Login Efetuado com Sucesso")
        time.sleep(5)
        jpas.destroy()
    else:
        lb["text"] = str("Senha incorreta")

passwd = Entry(jpas)
passwd.place(x=100, y=100)

confpas = Entry(jpas)
confpas.place(x=100, y=130)

btgravasenha = Button(jpas, text="GRAVA SENHA", width=20, command=bt_oksenha)
btgravasenha.place(x=100, y=170)
btentrar = Button(jpas, text="ENTRAR NO SISTEMA", width=20, command=bt_entrar)
btentrar.place(x=100, y=210)


lb = Label(jpas, text="Senha não cadastrado")
lb.place(x=100, y=250)

jpas.geometry("500x500+0+0")
jpas.mainloop()
#Encerra tela de login
#==================================================================

#Inicia programa tela principal
#==================================================================
janela = Tk()
janela.title("Meu Programa")

#Inicia tela do menu Iniciar
def bt_iniciar():
    janela2 = Tk()
    janela2.title("teste")
    janela2["bg"] = "red"
    janela2.geometry("700x300+0+0")
    janela2.mainloop()
#Encerra tela do menu iniciar

#Chama o processo de encerrar o programa
#==================================================================
def bt_sair():
    janela.destroy()
#==================================================================

#Cria os botoes na tela principal
#==================================================================
btIniciar = Button(janela, text='Iniciar', width=10, command=bt_iniciar)
btIniciar.place(x=0, y=0)
btConsultar = Button(janela, text='Consultar', width=10)
btConsultar.place(x=100, y=0)
btDefinir = Button(janela, text='Definir', width=10)
btDefinir.place(x=200, y=0)
btConfiguracoes = Button(janela, text='Configurações', width=10)
btConfiguracoes.place(x=300, y=0)
btSobre = Button(janela, text='Sobre', width=10)
btSobre.place(x=400, y=0)
btSair = Button(janela, text='Sair', width=10, command=bt_sair)
btSair.place(x=500, y=0)
#Encerra os botões na tela principal
#==================================================================

janela.geometry("1024x768+0+0")
janela.mainloop()
#Encerra a janela principal
#==================================================================

 