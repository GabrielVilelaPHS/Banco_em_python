import os
from validacoes import validar_nome, tranformar_espaco_underline, validar_senha, validar_data, validar_cpf, validar_email 
from bancoDeDados import cadastrar_usuario, verificar_ambiguidade_cpf, verificar_ambiguidade_email

def tela_cadastro(diretorio):
    os.system('cls')

    dados_cadastrais = {'nome' : '' ,'senha' : '', 'aniversario' : '' , 'cpf' : '' , 'email' :'', 'saldo' : '0'}

    print('---------CADASTRO-----------\n')

    print('OBS: DIGITE "sair" A QUALQUE MOMENTO PARA CANCELAR O CADASTRO\n')

    while(True):
        nome = input('NOME COMPLETO: ')
        
        if(nome == 'sair' or validar_nome(nome) == True):
            nome = tranformar_espaco_underline(nome, 'espaco')
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')
    
    if(nome == 'sair'):
        return

    while(True):
        senha = input('\nSENHA DA CONTA (NO MINIMO 5 E NO MAXIMO 12 CARACTERES): ')
        
        if(senha == 'sair' or validar_senha(senha) == True):
            break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(senha == 'sair'):
        return 

    while(True):
        aniversario = input('\nDATA DE ANIVERSÁRIO (PADRÃO DD/MM/AAAA): ')
        
        resultado_valida_data = validar_data(aniversario);

        if(aniversario == 'sair' or resultado_valida_data!= False):
            if(resultado_valida_data < 18):
                print('A IDADE MÍNIMA PARA CADASTRO É DE 18 ANOS')
            else:
                break
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(aniversario == 'sair'):
        return
    

    while(True):
        cpf = input('\nCPF (SOMENTE NÚMEROS): ')
        
        
        if(cpf == 'sair' or validar_cpf(cpf) == True ):
            if(verificar_ambiguidade_cpf(cpf, diretorio) == False):
                break
            else:
                print("CPF JA CADASTRADO, TENTE OUTRO")
                continue
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(cpf == 'sair'):
        return 


    while(True):
        email = input('\nEMAIL: ')
        
        if(email == 'sair' or valida_email(email) == True):
            if(verificar_ambiguidade_email(email, diretorio) == True):
                break
            else:
                print("EMAIL JA CADASTRADO, TENTE OUTRO")
                continue
        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE\n')

    if(email == 'sair'):
        return

    dados_cadastrais['nome'] = nome;
    dados_cadastrais['senha'] = senha;
    dados_cadastrais['aniversario'] = aniversario;
    dados_cadastrais['cpf'] = cpf;
    dados_cadastrais['email'] = email;

    print(f"nome: {dados_cadastrais['nome']}\n aniversario: {dados_cadastrais['aniversario']} \n cpf: {dados_cadastrais['cpf']} \n email: {dados_cadastrais['email']}")

    cadastrar_usuario(diretorio, dados_cadastrais)

