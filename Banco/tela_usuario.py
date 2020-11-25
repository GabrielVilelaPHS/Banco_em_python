import os

from tela_operacoes_bancarias import tela_operacoes_bancarias
from arquivo_alterar_informacoes import extrair_dados
from tela_configuracoes import tela_configuracoes
from validacoes import validar_menu

def tela_usuario(cpf, diretorio):

    dicionario = extrair_dados(cpf, diretorio)

    while(True):
        os.system('cls')
        print(f"---------------------- BEM VINDO {dicionario['Nome']} ----------------------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - OPÇÕES BANCARIAS")
        print("(02) - CONFIGURAÇÕES DO USUÁRIO")

        resposta = validar_menu(1, 2)

        controle_main(resposta, cpf, diretorio)

def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        tela_operacoes_bancarias(cpf, diretorio)
        

    elif (resposta == 2):
        tela_configuracoes(cpf, diretorio)