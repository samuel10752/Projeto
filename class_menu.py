from class_cadastro import*

class Menu(): 
    def __init__(self):
        cadastro = bancoDados()

        while True:
            entrada=input(f'1 - Cadastrar Usuário\n'
                        f'2 - Listar Usuários'
                        f'0 - Sair\n'
                        f': ')
            if entrada == '1':
                cpf_cnpj = input('CPF: ')
                nome = input('Nome: ')
                dataNasc = input('Data Nasc.: ')
                telefone = input('Tel.: ')
                senha = input('Senha.: ')

                #cpf_cnpj = "123.456.789-03"
                #nome = "Ewerson"
                #dataNasc = "1993/03/17"
                #telefone = "(035)9-9233-7155"
                #senha = "123456789"
                cadastro.cadastros(cpf_cnpj, nome, dataNasc, telefone, senha)
            elif entrada == '2':
                cadastro.listar_usuarios()
            elif entrada == '0':
                print('Obrigado por acessar. Até a próxima.')
            else:
                print('Opção invalida!!! Tente novamente.')