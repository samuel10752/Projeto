from tkinter import messagebox
import mysql.connector
from class_usuario import*
class Cadastro:

    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='investimentos')
        self.mycursor = self.conexao.cursor() 

    def cadastro(self,cpf_cnpj, nome, dataNasc, telefone, senha):
        cpf_cnpj = cpf_cnpj
        nome = nome
        dataNasc = dataNasc
        telefone = telefone
        senha = senha
        comando_sql = f'select * from Usuarios'
        self.mycursor.execute(comando_sql)
        lista = self.mycursor.fetchall()
        contador=0
        for i in lista:
            if cpf_cnpj == i[0]:
                contador=1
                messagebox.showinfo('', 'User já cadastrado')
                break
        if contador == 0:
            obj_cadastros = Usuario(cpf_cnpj, nome, dataNasc, telefone, senha)
            comando_sql = f"insert into Usuarios (cpf_cnpj, nome, dataNasc, telefone, senha) value ('{obj_cadastros.cpf_cnpj}','{obj_cadastros.nome}','{obj_cadastros.dataNasc}','{obj_cadastros.telefone}', '{obj_cadastros.senha}')"
            self.mycursor.execute(comando_sql)
            self.conexao.commit()
            messagebox.showinfo('', 'User foi cadastrado')
    
    #Inserção de moeda
    def cadastro_movimentacao(self, cod, nome_atk, nome_moeda, capital, meses, montante):
        self.cod = cod
        self.nome_atk = nome_atk
        self.nome_moeda = nome_moeda
        self.capital = capital 
        self.meses = meses
        self.montante = montante
        comando_sql = f'insert into Movimentacoes (cod, nome_atk, nome_moeda, capital, meses, montante) value ("{self.cod}", "{self.nome_atk}", "{self.nome_moeda}", "{self.capital}", "{self.meses}", "{self.montante}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        messagebox.showinfo('', 'Movimentação foi cadastrada')

    #Venda de moeda
    def cadastro_movimentacoes_n(self, cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n):
        self.cod_n = cod_n
        self.nome_atk_n = nome_atk_n
        self.nome_moeda_n = nome_moeda_n
        self.capital_n = capital_n
        self.montante_n = montante_n
        comando_sql = f'insert into Movimentacoes_n (cod_n, nome_atk_n, nome_moeda_n, capital_n, montante_n) value ("{self.cod_n}", "{self.nome_atk_n}", "{self.nome_moeda_n}", "{self.capital_n}", "{self.montante_n}")'
        self.mycursor.execute(comando_sql)
        self.conexao.commit()
        messagebox.showinfo('', 'Movimentação foi cadastrada')