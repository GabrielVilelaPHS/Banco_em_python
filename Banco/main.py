import os

from inicializacao import gerando_diretorio_com_pasta
from tela_login import tela_login
from tela_cadastro import tela_cadastro
from validacoes import validar_menu

def controle_main(tela_inicio, diretorio):

    if (tela_inicio == 1):
        tela_login(diretorio)

    elif (tela_inicio == 2):
        retorno = tela_cadastro(diretorio)

        if(retorno == True):
            print("\nCADASTRO REALIZADO COM SUCESSO\n")
            os.system('pause')

        elif(retorno == False):
            print("\nDESCULPE, HOUVE ERRO NA CRIAÇÃO DO USUÁRIO\nTENTE NOVAMENTE...\n")
            os.system('pause')

    elif (tela_inicio == 3):
        exit(0)

nome_pasta = "usuarios"
diretorio = gerando_diretorio_com_pasta(nome_pasta)

while(True):
    
    while(True):
        os.system('cls')
        print("---------------------- BEM VINDO ----------------------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - FAZER LOGIN")
        print("(02) - FAZER CADASTRO")
        print("(03) - SAIR")

        resposta = validar_menu(1, 3)

        controle_main(resposta, diretorio)


