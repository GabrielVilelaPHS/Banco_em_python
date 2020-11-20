import os

from arquivo_alterar_informacoes import extrair_dados
from capturar_campos import capturar_saldo_inteiro, capturar_campo_cpf, capturar_campo_nome
from bancoDeDados import verificar_ambiguidade_cpf
from validacoes import validar_cpf
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
    
    dicionario['Saldo'] = str (int (dicionario['Saldo']) + int (valor) )

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
    
    if not (valor_automatico):
        registar_historico(f"DEPOSITO: {int(valor)}\n\t.\n", cpf)
    return valor


def saque(cpf, diretorio, **kws):

    valor_automatico = kws.get('valor_automatico')
    
    os.system('cls')
    dicionario = extrair_dados(cpf, diretorio)

    if(int (dicionario['Saldo']) > 0):
        
        if(valor_automatico):
            valor = valor_automatico
        else:
            print('\n... DIGITE "sair" PARA CANCELAR O SAQUE...' )
            valor = capturar_saldo_inteiro(MAX =3000)

        if(valor.lower() == 'sair'):
            return valor
        
        dicionario['Saldo'] = str (int (dicionario['Saldo']) - int (valor) )

        if(int (dicionario['Saldo']) >= 0):

            caminho = f"{diretorio}//{cpf}.txt"

            with open(caminho, 'w') as arquivo:
                arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")

            if not (valor_automatico):
                registar_historico(f"SAQUE: De {int(valor)} reais\n\t.\n", cpf)
            return valor

        else:
            return False
            
    else:
        return False

def transferencia(cpf, diretorio, **kws):



    os.system('cls')
    print("...CONFIRME OS DADOS DO RECEPTOR...")
    print('........DIGITE "sair" PARA CANCELAR A TRAANSFERÊNCIA...\n' )
    os.system('pause')

    receptor_cpf = input('\nCPF (SOMENTE NÚMEROS): ')    
            
    if(receptor_cpf.lower() == 'sair'):
        return receptor_cpf

    elif(validar_cpf(receptor_cpf) ==  False):
        return False

    if(verificar_ambiguidade_cpf(receptor_cpf, diretorio) == True):

        remetente_dicionario = extrair_dados(cpf, diretorio)
        receptor_dicionario = extrair_dados(receptor_cpf, diretorio)

        receptor_nome = capturar_campo_nome()

        if(receptor_nome.lower() == "sair"):
            return receptor_nome

        if(receptor_dicionario['Nome'] == (receptor_nome.upper())):
            valor = saque(cpf, diretorio)

            if(valor != True and valor != False):
                if( deposito(receptor_cpf, diretorio, valor_automatico = valor)):
                    registar_historico(f"TRANFERENCIA: Pago {int(valor)} reais de {remetente_dicionario['Nome']}\n\t.\n", cpf)
                    registar_historico(f"TRANFRENCIA: Recebido {int(valor)} reais para {receptor_nome.upper()}\n\t.\n", receptor_cpf)
                    return True

    return False

    #os.path.dirname(os.path.abspath("path/to/project/foo.py"))

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