
import os
from verificar_login import coletar_dados_login, verificar_login
from tela_usuario import tela_usuario

def tela_login(diretorio):
    
    while(True):
        os.system('cls')
        print('---------------------- LOGIN ----------------------\n')
        print('OBS: DIGITE "voltar" A QUALQUE MOMENTO PARA VOLTAR A TELA INICIAL\n')

        dados ={}

        dados = coletar_dados_login()

        resposta = verificar_login(dados, diretorio)
    
        if (resposta == True):
            print("...LOGIN FEITO COM SUCESSO\n")
            os.system('pause')
            os.system('cls')   
            tela_usuario(dados['Cpf'], diretorio)

        elif(resposta == False):
            print("ENTRADA INVÁLIDA, VERIFIQUE O CPF E SENHA")
            os.system('pause')
        
        else:
            break
        