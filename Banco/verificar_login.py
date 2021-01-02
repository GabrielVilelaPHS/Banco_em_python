import os 
from validacoes import validar_cpf, validar_senha
from arquivo_manipula_dados import verificar_ambiguidade_cpf

def coletar_dados_login():

    dicionario = {}

    while(True):
        cpf = input('CPF (SOMENTE NÚMEROS): ')
        
        
        if(cpf == 'voltar' or validar_cpf(cpf) == True ):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(cpf == 'voltar'):
        return cpf

    while(True):
        senha = input('\nSENHA DA CONTA (NO MINIMO 5 E NO MAXIMO 12 CARACTERES): ')
        
        if(senha == 'voltar' or validar_senha(senha) == True):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(senha == 'voltar'):
        return senha

    dicionario['Cpf'] = cpf
    dicionario['Senha'] = senha

    return dicionario

def verificar_login(dados, diretorio):

    cpf = dados['Cpf']
    senha = dados['Senha']

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
                
                if(senha == auxiliar_senha):
                    return True
                else:
                    return False
    
    else:
        return False

def verificar_usuario(dicionario):
    os.system('cls')
    dados = {}

    print("\n...ANTES DE PROCEGUIR, CONFIRME QUE VOCÊ É O DONO DA CONTA\n")

    dados = coletar_dados_login()

    if(dados == "voltar"):
        return dados

    if(dicionario['Cpf'] == dados['Cpf'] and dicionario['Senha'] == dados['Senha']):
        return True
    else:
        return False




