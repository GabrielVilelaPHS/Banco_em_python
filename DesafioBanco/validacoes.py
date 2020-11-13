from datetime import datetime, date
'''
TELA DE CADASTRO
'''
def validar_nome(nome):

    if (nome.isnumeric()):
        return False

    return True

def tranformar_espaco_underline(nome, tipo):

    copia_nome = '';

    if(tipo == 'espaco'):
        for caracter in nome:
            if (caracter == ' '):
                copia_nome += '_'
            else: 
                copia_nome += caracter

    elif(tipo == 'underline'):
        for caracter in nome:
            if (caracter == '_'):
                copia_nome = ' '
            else: 
                copia_nome = caracter
    else:
        return None
    
    return copia_nome.upper()

def validar_senha(senha):

    if(len(senha) < 5 or len(senha) > 12):
        return False
    
    return True


def validar_data(data):

    if(data.isnumeric()):
        return False

    lista_data = data.split('/')

    if(len(lista_data) !=3):
        return False

    elif(len(lista_data[0]) != 2 and len(lista_data[1]) != 2 and len(lista_data[2]) != 4):
        return False
    
    dia = int (lista_data[0])
    mes = int (lista_data[1])
    ano = int (lista_data[2])

    if(dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano >2020):
        return False

    date_of_birth = datetime.strptime(f'{dia} {mes} {ano}', "%d %m %Y")

    idade = calcular_idade(date_of_birth)

    return idade

def calcular_idade(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def validar_cpf(cpf):

    if(cpf.isalpha() or len(cpf) != 11):
        return False
    
    return True


def validar_email(email):

    copia_email = email
    caracte_arroba = 0;
    lista_fim_email = email.split('.com')
    

    if(len(email) <=24 and len(lista_fim_email) == 2):

        for caracter in copia_email:
            if(caracter == '@'):
                caracte_arroba += 1
        
        if(caracte_arroba == 1):
            return True
        else:
            return False

    return False


    