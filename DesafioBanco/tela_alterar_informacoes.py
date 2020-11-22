import os
from arquivo_alterar_informacoes import extrair_dados, alterar_campo_nome, alterar_campo_senha, alterar_campo_aniversario, alterar_campo_email
from validacoes import validar_menu

def alterar_informacoes(cpf, diretorio):

    while(True):
        #os.system('cls')

        dicionario = extrair_dados(cpf, diretorio)

        print('--------- CONFIGURAÇÕES DE USUÁRIO --------\n')

        print('SEUS DADOS PESSOAIS: \n')
        print(f"Nome: {dicionario['Nome']}")
        print(f"SENHA: {dicionario['Senha']}")
        print(f"ANIVERSARIO: {dicionario['Aniversario']}")
        print(f"EMAIL: {dicionario['Email']}\n")


        print('\nVOCE DESEJA ALTERAR...\n')
        print(f'(01) - NOME ')
        print(f'(02) - SENHA ')
        print(f'(03) - ANIVERSARIO ')
        print(f'(04) - EMAIL ')
        print(f'(05) - VOLTAR')

        resposta = validar_menu(1, 5)
    
        if(resposta == 5):
            break

        controle_logico(resposta, cpf, diretorio)
        print("\nalterção feita com sucesso\n")
        os.system('pause')


def controle_logico(resposta, cpf, diretorio):

    if(resposta == 1):
        alterar_campo_nome(cpf, diretorio)

    elif(resposta == 2):
        alterar_campo_senha(cpf, diretorio)

    elif(resposta == 3):
        alterar_campo_aniversario(cpf, diretorio)

    elif(resposta == 4):
        alterar_campo_email(cpf, diretorio)