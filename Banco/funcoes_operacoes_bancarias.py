import os

from arquivo_alterar_informacoes import extrair_dados
from arquivo_manipula_dados import verificar_ambiguidade_cpf
from capturar_campos import capturar_saldo_inteiro, capturar_saldo_float, capturar_campo_cpf, capturar_campo_nome
from validacoes import validar_cpf
from funcao_verificar_login import verificar_usuario
from inicializacao import gerando_diretorio_com_pasta


def deposito(cpf, diretorio, **kws):
    
    os.system('cls')

    dicionario = extrair_dados(cpf, diretorio)

    valor_automatico = kws.get('valor_automatico')

    if(valor_automatico):
        valor = valor_automatico
    else:
        print('\n... DIGITE "voltar" PARA CANCELAR O DEPOSITO...' )
        valor = capturar_saldo_inteiro(MAX = 5000)

    if(valor == 'voltar'):
        return valor
    
    dicionario['Saldo'] = str (float (dicionario['Saldo']) + float (valor) )

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
    
    if not (valor_automatico):
        registar_historico(f"DEPOSITO: {int(valor)}\n\t.\n", cpf)
    return valor


def saque(cpf, diretorio, **kws):

    valor_tranferido = kws.get('valor_tranferido')    
    
    os.system('cls')
    dicionario = extrair_dados(cpf, diretorio)
    dicionario['Cpf'] = cpf

    if(float (dicionario['Saldo']) > 0):
        
        if(valor_tranferido):
            valor = valor_tranferido

        else:
            print('\n... DIGITE "voltar" PARA CANCELAR O SAQUE...' )
            valor = capturar_saldo_inteiro(MAX =3000)

            teste = verificar_usuario(dicionario)

            if (teste == False or teste == "voltar"):
                return teste

        if(valor.lower() == 'voltar'):
            return valor

        dicionario['Saldo'] = (float (dicionario['Saldo']) - float (valor) )

        round(dicionario['Saldo'], 2)

        dicionario['Saldo'] = str (dicionario['Saldo'])


        if(float (dicionario['Saldo']) >= 0):

            caminho = f"{diretorio}//{cpf}.txt"

            with open(caminho, 'w') as arquivo:
                arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")

            if not (valor_tranferido):
                registar_historico(f"SAQUE: De {int(valor)} reais\n\t.\n", cpf)
            return valor

        else:
            return False
            
    else:
        return False

def transferencia(cpf, diretorio, **kws):

    os.system('cls')
    print("...CONFIRME OS DADOS DO RECEPTOR...")
    print('........DIGITE "voltar" PARA CANCELAR A TRANSFERÊNCIA...\n' )

    receptor_cpf = input('\nCPF (SOMENTE NÚMEROS): ')    
            
    if(receptor_cpf.lower() == 'voltar'):
        return receptor_cpf

    elif(validar_cpf(receptor_cpf) ==  False):
        return False

    if(verificar_ambiguidade_cpf(receptor_cpf, diretorio) == True):

        remetente_dicionario = extrair_dados(cpf, diretorio)
        receptor_dicionario = extrair_dados(receptor_cpf, diretorio)

        receptor_nome = capturar_campo_nome()

        if(receptor_nome.lower() == "voltar"):
            return receptor_nome

        if(receptor_dicionario['Nome'] == (receptor_nome.upper())):
            valor_tranferido = capturar_saldo_float(MAX = 3000)

            string_valor = str (valor_tranferido)

            if(string_valor.lower() == 'voltar'):
                return string_valor.lower()

            print('entrou \n')

            valor = saque(cpf, diretorio, valor_tranferido = valor_tranferido)

            if(valor != True and valor != False):
                if( deposito(receptor_cpf, diretorio, valor_automatico = valor)):
                    registar_historico(f"TRANFERENCIA: Pago {float(valor)} reais para {remetente_dicionario['Nome']}\n\t.\n", cpf)
                    registar_historico(f"TRANFRENCIA: Recebido {float(valor)} reais de {receptor_nome.upper()}\n\t.\n", receptor_cpf)
                    return True

    return False


def extrato(cpf):

    diretorio = gerando_diretorio_com_pasta("extratos")
    
    nome_arquivo = f"{cpf}.txt"
    caminho = f"{diretorio}//{nome_arquivo}"

    lista_arquivos = os.listdir(diretorio) 
    
    for item in lista_arquivos:
        if( item == nome_arquivo):
            with open(caminho) as f:
                conteudo = f.read()

            return conteudo
    
    return False

def registar_historico(conteudo, cpf):

    diretorio = gerando_diretorio_com_pasta("extratos")

    nome_arquivo = f"{cpf}.txt"
    caminho = f"{diretorio}//{nome_arquivo}"

    lista_arquivos = os.listdir(diretorio) 
    
    flag = 0

    for item in lista_arquivos:
        if( item == nome_arquivo):
            flag = 1
            break
                    
    if(flag ==  0):

        with open(caminho, 'w') as f:
            f.write(conteudo)
    
    elif(flag == 1):
        with open(caminho, 'a') as f:
            f.write(conteudo)