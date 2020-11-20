from inicializacao import gerando_diretorio_com_pasta
from tela_login import tela_login
from tela_cadastro import tela_cadastro
import os

def controle_main(tela_inicio, diretorio):

    if (tela_inicio == 1):
        tela_login(diretorio)
        pass

    elif (tela_inicio == 2):
        tela_cadastro(diretorio)

    elif (tela_inicio == 3):
        exit(0)

banco_de_dados = "usuarios"
diretorio_banco_de_dados = gerando_diretorio_com_pasta(banco_de_dados)
sessao = 0

while(sessao == 0):
    
    while(True):
        os.system('cls')
        print("--------- BEM VINDO --------\n")
        print("O QUE VOCÊ DESEJA:")
        print("(01) - FAZER LOGIN")
        print("(02) - FAZER CADASTRO")
        print("(03) - SAIR")

        while(True):
            try:
                resposta = int (input("\nRESPOSTA: "))

            except (ValueError, AttributeError):
                print('DIGITE UM NUMERO INTEIRO')
                os.system('pause')
                continue

            boleano = str (resposta)

            if(boleano.isnumeric() and (resposta < 1 or resposta > 3 )):
                print("NUMERO FORA DO INTERVALO")
                os.system('pause')
                continue
            break

        controle_main(resposta, cpf, diretorio)


#controleMain(resposta_tela_inicio)

