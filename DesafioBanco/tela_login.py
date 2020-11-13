
import os
from validacoes import validar_cpf, validar_senha
from bancoDeDados import verificar_login

def tela_login(diretorio):
    os.system('cls')
    print('---------LOGIN-----------\n')
    print('OBS: DIGITE "voltar" A QUALQUE MOMENTO PARA VOLTAR A TELA INICIAL\n')
    
    while(True):
        cpf = input('\nCPF (SOMENTE NÚMEROS): ')
        
        
        if(cpf == 'voltar' or validar_cpf(cpf) == True ):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(cpf == 'voltar'):
        return 

    while(True):
        senha = input('\nSENHA DA CONTA (NO MINIMO 5 E NO MAXIMO 12 CARACTERES): ')
        
        if(senha == 'voltar' or validar_senha(senha) == True):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(senha == 'voltar'):
        return 

    #print('aaaaaaaaaaaaaa')
    if(verificar_login(cpf, senha, diretorio) == True):

        print("login feito")
        os.system('pause')

    else:

        print("ENTRADA INVÁLIDA, VERIFIQUE O CPF E SENHA")
        os.system('pause')
        