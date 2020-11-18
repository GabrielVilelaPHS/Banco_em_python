import os

from capturar_campos import capturar_campo_nome, capturar_campo_senha, capturar_campo_aniversario, capturar_campo_email
def extrair_dados(cpf, diretorio):
    
    dicionario = {}

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho) as arquivo:

        for line in arquivo:
            lista_sem_barra_n = line.split('\n')
            lista_sem_dois_pontos = lista_sem_barra_n[0].split(':')
            dicionario[lista_sem_dois_pontos[0]] = lista_sem_dois_pontos[1] 

    return dicionario

def alterar_campo_nome(cpf, diretorio):

    dicionario = extrair_dados(cpf, diretorio)
    nome = capturar_campo_nome()

    dicionario['Nome'] = nome

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")

def alterar_campo_senha(cpf, diretorio):
    dicionario = extrair_dados(cpf, diretorio)
    senha = capturar_campo_senha()

    os.system('pause')
    dicionario['Senha'] = senha

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")

def alterar_campo_aniversario(cpf, diretorio):
    dicionario = extrair_dados(cpf, diretorio)
    aniversario = capturar_campo_aniversario()

    dicionario['Aniversario'] = aniversario

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")

def alterar_campo_email(cpf, diretorio):
    dicionario = extrair_dados(cpf, diretorio)
    email = capturar_campo_email(diretorio)

    dicionario['Email'] = email

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")



