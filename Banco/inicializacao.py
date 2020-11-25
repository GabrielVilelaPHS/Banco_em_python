import os

def gerando_diretorio_com_pasta(nome) :
    nome_pasta = nome
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lista_pastas_existentes = os.listdir(dir_path)
    flag = 0
    for pasta in lista_pastas_existentes:
        if(nome_pasta == pasta):
            flag = 1
            break
                    
    if(flag ==  0):
        os.mkdir(f'{nome_pasta}')
        print('Não foi encontrado pasta "arquivo", por isso a criamos para o programa rodar sem problemas!\n')
        os.system('pause')
        os.system('cls')

    diretorio = f'{dir_path}\\{nome_pasta}'

    return (diretorio)