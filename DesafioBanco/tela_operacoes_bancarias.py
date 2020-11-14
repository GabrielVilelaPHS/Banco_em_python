import os
from arquivo_operacoes_bancarias import saque, deposito, transferencia, extrato

def tela_operacoes_bancarias(cpf, diretorio):
    while(True):
        os.system('cls')
        print("--------- OPERAÇÕES BANCARIAS --------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - DEPÓSITO")
        print("(02) - SAQUE")
        print("(03) - TRANFERÊNCIA")
        print("(04) - EXTRATO")

        resposta = input("\nRESPOSTA: ")

        if(resposta.isnumeric()):

            resposta = int (resposta)

            if(resposta >= 1 and resposta <= 4):
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
        deposito(cpf, diretorio)
        
    elif (resposta == 2):
        saque(cpf, diretorio)
    
    elif (resposta == 3):
        transferencia(cpf, diretorio)

    elif (resposta == 4):
        extrato(cpf, diretorio)