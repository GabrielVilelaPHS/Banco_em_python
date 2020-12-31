import os
from arquivo_alterar_informacoes import extrair_dados, alterar_campo_senha,alterar_campo_email
from validacoes import validar_menu

def alterar_informacoes(cpf, diretorio):

    while(True):
        os.system('cls')

        dicionario = extrair_dados(cpf, diretorio)

        print('--------- CONFIGURAÇÕES DE USUÁRIO --------\n')

        print('SEUS DADOS PESSOAIS: \n')
        print(f"SENHA: {dicionario['Senha']}")
        print(f"EMAIL: {dicionario['Email']}\n")


        print('\nVOCE DESEJA ALTERAR...\n')
        print(f'(01) - SENHA ')
        print(f'(02) - EMAIL ')
        print(f'(03) - VOLTAR')

        resposta = validar_menu(1, 3)
    
        if(resposta == 3):
            break

        controle_logico(resposta, cpf, diretorio)


def controle_logico(resposta, cpf, diretorio):
    print("\nDigite 'voltar' se deseja cancelar a ação")

    if(resposta == 1):
        alterar_campo_senha(cpf, diretorio)

    elif(resposta == 2):
        alterar_campo_email(cpf, diretorio)