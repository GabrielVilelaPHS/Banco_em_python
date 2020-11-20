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


        while(True):
            try:
                resposta = int (input("\nRESPOSTA: "))

            except (ValueError, AttributeError):
                print('DIGITE UM NUMERO INTEIRO')
                os.system('pause')
                continue

            boleano = str (resposta)

            if(boleano.isnumeric() and resposta != 1 and resposta != 2 ):
                print("NUMERO FORA DO INTERVALO")
                os.system('pause')
                continue
            break

        controle_main(resposta, cpf, diretorio)

def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        tela_operacoes_bancarias(cpf, diretorio)
        

    elif (resposta == 2):
        tela_configuracoes(cpf, diretorio)