import os

from arquivo_alterar_informacoes import extrair_dados
from capturar_campos import capturar_saldo_inteiro

def deposito(cpf, diretorio):
    
    os.system('cls')

    dicionario = extrair_dados(cpf, diretorio)
    saldo = capturar_saldo_inteiro(MAX = 5000)

    if(saldo == 'voltar'):
        return saldo
    
    dicionario['Saldo'] = str (int (dicionario['Saldo']) + int (saldo) )

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho, 'w') as arquivo:
        arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
    
    return True


def saque(cpf, diretorio):
    
    os.system('cls')
    dicionario = extrair_dados(cpf, diretorio)

    if(int (dicionario['Saldo']) > 0):

        saldo = capturar_saldo_inteiro(MAX = 3000)

        if(saldo == 'voltar'):
            return saldo
        
        dicionario['Saldo'] = str (int (dicionario['Saldo']) - int (saldo) )

        if(int (dicionario['Saldo']) >= 0):

            caminho = f"{diretorio}//{cpf}.txt"

            with open(caminho, 'w') as arquivo:
                arquivo.write(f"Nome:{dicionario['Nome']}\nSenha:{dicionario['Senha']}\nAniversario:{dicionario['Aniversario']}\nEmail:{dicionario['Email']}\nSaldo:{dicionario['Saldo']}\n")
                
            return True

        else:
            return False
            
    else:
        return False

def transferencia(cpf, diretorio):
    pass

def extrato(cpf, diretorio):
    pass
