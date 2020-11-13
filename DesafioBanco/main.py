#cd Desktop/Python/DesafioBanco/
#python main.py
from inicializacao import gerando_diretorio_com_pasta
from tela_login import tela_login
from tela_cadastro import tela_cadastro
import os

def controle_main(tela_inicio, diretorio):

    if (tela_inicio == 1):
        tela_login(diretorio)
        pass

    if (tela_inicio == 2):
        tela_cadastro(diretorio)

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

        resposta_tela_inicio = input("\nRESPOSTA: ")

        if(resposta_tela_inicio.isnumeric()):

            resposta_tela_inicio = int (resposta_tela_inicio)

            if(resposta_tela_inicio == 1 or resposta_tela_inicio == 2):
                controle_main(resposta_tela_inicio, diretorio_banco_de_dados)

        elif(resposta_tela_inicio == '3'):
            os.cls()
            print('OBRIGADO POR CONFIAR NO NOSSO BANCO!!!')
            os.system('pause')

        else:
            print('ENTRADA INVÁLIDA, TENTE NOVAMENTE')
            os.system('pause')
            os.cls()
            continue



#controleMain(resposta_tela_inicio)

