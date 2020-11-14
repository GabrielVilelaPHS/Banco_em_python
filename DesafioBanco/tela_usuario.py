import os

from tela_operacoes_bancarias import tela_operacoes_bancarias
from tela_configuracoes import tela_configuracoes

def tela_usuario(cpf, diretorio):
    while(True):
        os.system('cls')
        print("--------- BEM VINDO FULANO --------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - OPÇÕES BANCARIAS")
        print("(02) - CONFIGURAÇÕES DO USUÁRIO")

        resposta = input("\nRESPOSTA: ")

        if(resposta.isnumeric()):

            resposta = int (resposta)

            if(resposta == 1 or resposta == 2):
                controle_main(resposta, cpf, diretorio)
            else:
                print("\nOPÇÃO NÃO EXISTENTE")

        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE')
            os.system('pause')
            os.cls()
            continue


def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        tela_operacoes_bancarias(cpf, diretorio)
        

    if (resposta == 2):
        tela_configuracoes(cpf, diretorio)