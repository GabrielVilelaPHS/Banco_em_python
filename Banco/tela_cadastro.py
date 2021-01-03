import os

from capturar_campos import capturar_campo_nome, capturar_campo_senha, capturar_campo_cpf, capturar_campo_aniversario, capturar_campo_email
from arquivo_manipula_dados import cadastrar_usuario

def tela_cadastro(diretorio):
    os.system('cls')

    dados_cadastrais = {'Nome' : '' ,'Senha' : '', 'Aniversario' : '' , 'Cpf' : '' , 'Email' :'', 'Saldo' : '0'}

    print('---------------------- CADASTRO----------------------\n')

    print('OBS: DIGITE "voltar" A QUALQUE MOMENTO PARA CANCELAR O CADASTRO\n')
    
    nome = capturar_campo_nome()
    
    if(nome.lower() == 'voltar'):
        return nome.lower()


    senha = capturar_campo_senha()

    if(senha == 'voltar'):
        return senha.lower()
        


    aniversario = capturar_campo_aniversario()

    if(aniversario == 'voltar'):
        return aniversario.lower()


    cpf = capturar_campo_cpf(diretorio)

    if(cpf == 'voltar'):
        return cpf.lower()


    email = capturar_campo_email(diretorio)

    if(email == 'voltar'):
        return email.lower()

    dados_cadastrais['Nome'] = nome;
    dados_cadastrais['Senha'] = senha;
    dados_cadastrais['Aniversario'] = aniversario;
    dados_cadastrais['Cpf'] = cpf;
    dados_cadastrais['Email'] = email;

    print(f"\nnome: {dados_cadastrais['Nome']} \naniversario: {dados_cadastrais['Aniversario']} \ncpf: {dados_cadastrais['Cpf']} \nemail: {dados_cadastrais['Email']}")

    return cadastrar_usuario(diretorio, dados_cadastrais)


