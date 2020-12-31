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

def alterar_campo_senha(cpf, diretorio):
    dicionario = extrair_dados(cpf, diretorio)
    senha = capturar_campo_senha()

    dicionario['Senha'] = senha

    caminho = f"{diretorio}//{cpf}.txt"

    if (senha.lower() == "voltar"):
        print("\nAÇÃO CANCELADA\n")

    else:
        with open(caminho, 'w') as arquivo:
            arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
        
        print("\nALTERAÇÃO FEITA COM SUCESSO\n")
    
    os.system('pause')

def alterar_campo_email(cpf, diretorio):
    dicionario = extrair_dados(cpf, diretorio)
    email = capturar_campo_email(diretorio)

    dicionario['Email'] = email

    caminho = f"{diretorio}//{cpf}.txt"

    if (email.lower() == "voltar"):
        print("\nAÇÃO CANCELADA\n")
    else:
        with open(caminho, 'w') as arquivo:
            arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
            
        print("\nALTERAÇÃO FEITA COM SUCESSO\n")
    
    os.system('pause')

    


