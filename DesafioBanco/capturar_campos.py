import os
from validacoes import validar_nome, validar_senha, validar_data, validar_cpf, validar_email, validar_saldo_inteiro
from bancoDeDados import verificar_ambiguidade_cpf, verificar_ambiguidade_email

def capturar_campo_nome():
    while(True):
        nome = input('NOME COMPLETO: ')
            
        if(nome == 'sair' or validar_nome(nome) == True):
            return nome.upper()
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

def capturar_campo_senha():
    while(True):
        senha = input('\nSENHA DA CONTA (NO MINIMO 5 E NO MAXIMO 12 CARACTERES): ')
        
        os.system('pause')
        if(senha == 'sair' or validar_senha(senha) == True):
            return senha
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')
    
def capturar_campo_aniversario():
    while(True):
        aniversario = input('\nDATA DE ANIVERSÁRIO (PADRÃO DD/MM/AAAA): ')
        
        resultado_valida_data = validar_data(aniversario);

        if(aniversario == 'sair' or resultado_valida_data!= False):
            if(resultado_valida_data < 18):
                print('A IDADE MÍNIMA PARA CADASTRO É DE 18 ANOS')
            else:
                return aniversario
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

def capturar_campo_cpf(diretorio):
    while(True):
        cpf = input('\nCPF (SOMENTE NÚMEROS): ')    
            
        if(cpf == 'sair' or validar_cpf(cpf) == True ):
            if(verificar_ambiguidade_cpf(cpf, diretorio) == False):
                return cpf
            else:
                print("CPF JA CADASTRADO, TENTE OUTRO")
                continue
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

def capturar_campo_email(diretorio):
    while(True):
        email = input('\nEMAIL: ')
        
        if(email == 'sair' or validar_email(email) == True):
            if(verificar_ambiguidade_email(email, diretorio) == True):
                return email
            else:
                print("EMAIL JA CADASTRADO, TENTE OUTRO")
                continue
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

def capturar_saldo_inteiro(MAX):
    print('\nDIGITE "voltar" SE DESEJA CANCELAR A AÇÃO')

    while(True):

        saldo = input('\nDIGITE O VALOR: ')

        if(saldo == 'voltar' or validar_saldo_inteiro(saldo) == True):
            
            if(saldo == 'voltar'):
                return saldo

            elif(len(saldo) <= 4 and int (saldo) <= MAX):
                return saldo

            elif(MAX == 5000):
                print(f"DEPÓSITO MÁXIMO DE {MAX} REAIS POR VEZ")

            elif(MAX == 3000):
                print(f"SAQUE MAXIMO DE {MAX} POR VEZ")
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')
            continue