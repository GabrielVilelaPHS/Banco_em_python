import os

from capturar_campos import capturar_campo_nome, capturar_campo_senha, capturar_campo_aniversario, capturar_campo_email
from funcao_verificar_login import verificar_usuario


def extrair_dados(cpf, diretorio):
    
    dicionario = {}

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho) as arquivo:

        for line in arquivo:
            lista_sem_barra_n = line.split('\n')
            lista_sem_dois_pontos = lista_sem_barra_n[0].split(':')
            dicionario[lista_sem_dois_pontos[0]] = lista_sem_dois_pontos[1] 

    return dicionario

def alterar_campo_senha(cpf, diretorio):

    dicionario = extrair_dados(cpf, diretorio)
    dicionario['Cpf'] = cpf

    senha = capturar_campo_senha()

    if (senha.lower() == "voltar"):
        print("\nAÇÃO CANCELADA\n")
        return senha.lower()
    
    teste = verificar_usuario(dicionario) 
    if (teste == False or teste == "voltar"):
        return teste
    
    dicionario['Senha'] = senha
    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
        
    print("\nALTERAÇÃO FEITA COM SUCESSO\n")
    
    os.system('pause')

def alterar_campo_email(cpf, diretorio):

    dicionario = extrair_dados(cpf, diretorio)
    dicionario['Cpf'] = cpf

    email = capturar_campo_email(diretorio)

    if (email.lower() == "voltar"):
        print("\nAÇÃO CANCELADA\n")
        return email.lower()

    if (verificar_usuario(dicionario) == False):
        return False

    dicionario['Email'] = email
    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
            
    print("\nALTERAÇÃO FEITA COM SUCESSO\n")
    
    os.system('pause')


def excluir_conta(cpf, diretorio):

    dicionario = extrair_dados(cpf, diretorio)
    dicionario['Cpf'] = cpf

    nome = f"{cpf}.txt"
    conta = f"{diretorio}\\{nome}"

    if (verificar_usuario(dicionario) == False):
        return False

    os.remove(conta)

    pastaMain = os.path.dirname(diretorio)
    pastaExtrato = f"{pastaMain}\\extratos"

    lista_arquivos = os.listdir(pastaExtrato)
    
    for arquivo in lista_arquivos:
        if(arquivo == nome):
            os.remove(f"{pastaExtrato}\\{nome}")
            
    print("\nCONTA APAGADA COM SUCESSO\n")
    
    os.system('pause')


