import os

from funcoes_operacoes_bancarias import deposito, saque, transferencia, extrato
from validacoes import validar_menu

def tela_operacoes_bancarias(cpf, diretorio):
    while(True):
        os.system('cls')
        print("---------------------- OPERAÇÕES BANCARIAS ----------------------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - SAQUE")
        print("(02) - EXTRATO")
        print("(03) - DEPÓSITO")
        print("(04) - TRANFERÊNCIA")
        print("(05) - VOLTAR")

        resposta = validar_menu(1, 5)
    
        if(resposta == 5):
            break

        controle_main(resposta, cpf, diretorio)


def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        confirmacao = saque(cpf, diretorio)
        
        if(confirmacao.isnumeric()):
            print("...SAQUE FEITO COM SUCESSO")
        elif(confirmacao == False):
            print("...DESCULPE, ALGO DEU ERRADO...\n...VERIFIQUE SEU SALDO PARA VER SE TEM SALDO SUFICIENTE...")
        
        os.system('pause')
    
    elif (resposta == 2):
        conteudo = extrato(cpf)

        if(extrato != False):
            os.system('cls')
            if(len(conteudo) != 0):
                print (conteudo)
            else:
                print("SEM HISTORICO BANCÁRIO\n")
        else:
            print("\n...DESCULPE, ALGO DEU ERRADO...")

        os.system('pause')

    elif (resposta == 3):
        confirmacao = deposito(cpf, diretorio) 

        if(confirmacao.isnumeric() ):
            print("...DEPOSITO FEITO COM SUCESSO")
        elif(confirmacao == False):
            print("...DESCULPE, ALGO DE ERRADO, TENTE MAIS TARDE")
        
        os.system('pause')
    
    elif (resposta == 4):
        confirmacao = transferencia(cpf, diretorio)

        if(confirmacao == True):
            print("\n...TRANFERÊNCIA FEITO COM SUCESSO")
        elif(confirmacao == False):
            print("\n...DESCULPE, ALGO DEU ERRADO...\n...VERIFIQUE OS DADOS DO RECEPTOR...\n")
        
        os.system('pause')
