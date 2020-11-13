import os

def cadastrar_usuario(diretorio, dados):

    nome_arquivo = dados['cpf'] + ".txt"
    caminho = f"{diretorio}\\{dados['cpf']}.txt"
    arquivo = open(caminho,'w')    

    conteudo_arquivo = f"Nome:{dados['nome']}\nSenha:{dados['senha']}\nAniversario:{dados['aniversario']}\nEmail:{dados['email']}\nSaldo:{dados['saldo']}\n"

    arquivo.write(conteudo_arquivo)

    arquivo.close()

def verificar_ambiguidade_cpf(campo, diretorio):

    if(campo.isnumeric()):

        cpf = campo + ".txt"

        lista_cpf = os.listdir(diretorio)

        if(len(lista_cpf) == 0):
            return False

        for nome_arquivo in lista_cpf:
            if(nome_arquivo == cpf):
                return True
        
        return False

def verificar_ambiguidade_email(email, diretorio):

    lista_arquivo = os.listdir(diretorio)
    lista_email = []

    if(len(lista_arquivo) == 0):
        return True

    for nome_arquivo in lista_arquivo:

        caminho = f"{diretorio}\\{nome_arquivo}"

        arquivo = open(caminho, 'r')
        conteudo_arquivo = arquivo.readlines()
        arquivo.close()

        extracao = extrair_email(conteudo_arquivo)
        
        if(extracao != False):
            lista_email.append(extracao)


    for item in lista_email:

        if(item == email):
            return False

    return True


def extrair_email(conteudo_arquivo):
    
    dados = conteudo_arquivo

    for item in dados:
        lista_item = item.split(':')

        if(lista_item[0] == "Email"):

            lista_email = lista_item[1].split("\n")
            email = lista_email[0]
            
            return email

    return False

def verificar_login(cpf, senha, diretorio):

    copia_senha = senha

    if(verificar_ambiguidade_cpf(cpf, diretorio) == True):

        lista_item = []

        nome_arquivo = cpf + ".txt"
        caminho = f"{diretorio}\\{nome_arquivo}"

        arquivo = open(caminho, 'r')
        conteudo_arquivo = arquivo.readlines()
        arquivo.close()

        
        for item in conteudo_arquivo:
            lista_item = item.split(':')

            if(lista_item[0] == "Senha"):

                lista_senha = lista_item[1].split("\n")
                auxiliar_senha = lista_senha[0]
                
                if(copia_senha == auxiliar_senha):
                    return True
                else:
                    return False
    
    else:
        return False
