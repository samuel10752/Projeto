#Informações Para Cadastro
class Usuario():
    def __init__ (self, cpf_cnpj, nome, dataNasc, telefone, senha):
        self.cpf_cnpj = cpf_cnpj
        self.nome = nome
        self.dataNasc = dataNasc
        self.telefone = telefone
        self.senha = senha
