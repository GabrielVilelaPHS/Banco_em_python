
import os
from validacoes import validar_cpf, validar_senha
from bancoDeDados import verificar_login
from tela_usuario import tela_usuario

def tela_login(diretorio):
    os.system('cls')
    print('---------LOGIN-----------\n')
    print('OBS: DIGITE "voltar" A QUALQUE MOMENTO PARA VOLTAR A TELA INICIAL\n')
    
    while(True):
        cpf = "11111111111"#input('CPF (SOMENTE NÚMEROS): ')
        
        
        if(cpf == 'voltar' or validar_cpf(cpf) == True ):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(cpf == 'voltar'):
        return 

    while(True):
        senha = "12345"#input('\nSENHA DA CONTA (NO MINIMO 5 E NO MAXIMO 12 CARACTERES): ')
        
        if(senha == 'voltar' or validar_senha(senha) == True):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(senha == 'voltar'):
        return 

    #print('aaaaaaaaaaaaaa')
    if(verificar_login(cpf, senha, diretorio) == True):
        print("...LOGIN FEITO COM SUCESSO\n")
        os.system('pause')
        os.system('cls')
        tela_usuario(cpf, diretorio)

    else:

        print("ENTRADA INVÁLIDA, VERIFIQUE O CPF E SENHA")
        os.system('pause')
        