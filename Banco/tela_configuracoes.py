import os
import sys
from tela_alterar_informacoes import alterar_informacoes
from validacoes import validar_menu

def tela_configuracoes(cpf, diretorio):
    while(True):
        os.system('cls')
        print("---------------------- CONFIGURAÇÕES DE USUÁRIO ----------------------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - ALTERAR INFORMAÇÕES PESSOAIS")
        print("(02) - SAIR DA CONTA")
        print("(03) - VOLTAR")

        resposta = validar_menu(1, 3)
        
        controle_main(resposta, cpf, diretorio)

        if(resposta == 3):
            break

def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        alterar_informacoes(cpf, diretorio)
        
    elif (resposta == 2):
        exit(0)
    