import os
from tela_alterar_informacoes import alterar_informacoes

def tela_configuracoes(cpf, diretorio):
    while(True):
        os.system('cls')
        print("--------- CONFIGURAÇÕES DE USUÁRIO --------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - ALTERAR INFORMAÇÕES PESSOAIS")
        print("(02) - SAIR DA CONTA")


        resposta = input("\nRESPOSTA: ")

        if(resposta.isnumeric()):

            resposta = int (resposta)

            if(resposta == 1 or resposta == 2):
                controle_main(resposta, cpf, diretorio)
                break
            else:
                print("\nOPÇÃO NÃO EXISTENTE")
                os.system('pause')

        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE')
            os.system('pause')
            os.cls()


def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        alterar_informacoes(cpf, diretorio)
        
    elif (resposta == 2):
        exit()
    