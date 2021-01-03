import os
from tela_alterar_informacoes import alterar_informacoes
from arquivo_alterar_informacoes import excluir_conta
from validacoes import validar_menu

def tela_configuracoes(cpf, diretorio):
    while(True):
        os.system('cls')
        print("---------------------- CONFIGURAÇÕES DE USUÁRIO ----------------------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - ALTERAR INFORMAÇÕES PESSOAIS")
        print("(02) - APAGAR CONTA")
        print("(03) - SAIR DA CONTA")
        print("(04) - VOLTAR")

        resposta = validar_menu(1, 4)
        
        controle_main(resposta, cpf, diretorio)

        if(resposta == 4):
            break

def controle_main(resposta, cpf, diretorio):

    if (resposta == 1):
        alterar_informacoes(cpf, diretorio)
    
    elif (resposta == 2):
        excluir_conta(cpf, diretorio)
        exit(0)

    elif (resposta == 3):
        exit(0)

    