import os

def extrair_dados(cpf, diretorio):
    
    dicionario = {}

    caminho = f"{diretorio}//{cpf}.txt"

    with open(caminho) as arquivo:

        for line in arquivo:
            lista_sem_barra_n = line.split('\n')
            lista_sem_dois_pontos = lista_sem_barra_n[0].split(':')
            dicionario[lista_sem_dois_pontos[0]] = lista_sem_dois_pontos[1] 

    return dicionario
    
    


