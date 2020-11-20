import os
import sys
from tela_alterar_informacoes import alterar_informacoes

def tela_configuracoes(cpf, diretorio):
    while(True):
        os.system('cls')
        print("--------- CONFIGURAÇÕES DE USUÁRIO --------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - ALTERAR INFORMAÇÕES PESSOAIS")
        print("(02) - SAIR DA CONTA")
        print("(03) - VOLTAR")


        while(True):
            try:
                resposta = int (input("\nRESPOSTA: "))

            except (ValueError, AttributeError):
                print('DIGITE UM NUMERO INTEIRO')
            
            finally:
            
                if(resposta < 1 and resposta >3 ):
                    print("NUMERO FORA DO INTERVALO")
                    os.system('pause')
                    continue
                
            break
        
        if(resposta == 3):
            break
        
        controle_main(resposta, cpf, diretorio)

        #os._exit(0)


def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        alterar_informacoes(cpf, diretorio)
        
    elif (resposta == 2):
        exit(0)
    