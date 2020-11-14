import os
from arquivo_alterar_informacoes import extrair_dados

def alterar_informacoes(cpf, diretorio):

    while(True):
        #os.system('cls')

        dicionario = extrair_dados(cpf, diretorio)

        print('--------- CONFIGURAÇÕES DE USUÁRIO --------\n')

        print('SEUS DADOS PESSOAIS: \n')
        print(f"Nome: {dicionario['Nome']}")
        print(f"CPF: {cpf}")
        print(f"ANIVERSARIO: {dicionario['Aniversario']}")
        print(f"EMAIL: {dicionario['Email']}\n")

        print('\nVOCE DESEJA ALTERAR...\n')
        print(f'(01) - NOME ')
        print(f'(02) - CPF ')
        print(f'(03) - ANIVERSARIO ')
        print(f'(04) - EMAIL ')
        print(f'(05) - TUDO MENOS O CPF')

        while(True):
            try:
                resposta = int (input("\nRESPOSTA: "))

            except (ValueError, AttributeError):
                print('DIGITE UM NUMERO INTEIRO')
            
            finally:
            
                print(resposta)
                if(resposta >= 1 and resposta <=5 ):
                    break
                else:
                    print("NUMERO FORA DO INTERVALO")
                    os.system('pause')
                    continue

    controle_logico(resposta, cpf, diretorio)


def controle_logico(funcao, cpf, diretorio):

    switch(funcao){
        case 1:
            altera_campo('Nome', cpf, diretorio)
            break
        case 2:
            renomear_pasta(cpf, diretorio)
            break
        case 3:
            altera_campo('Aniversario', cpf, diretorio)
            break
        case 4:
            altera_campo('Email', cpf, diretorio)
            break
        case 5:
            altera_campo('Tudo', cpf, diretorio)
            break
    }