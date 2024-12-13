users = [[]]
events = []
def verificar_senha(senha1, senha2):
    if(senha1 != senha2):
        return True
    else:
        return False

def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if(user[1] == email):
            existe = True
            break
    return existe

def inserir_usuario(usuario, lista_usuarios):
    lista_usuarios.append(usuario)

def ler_info_usuario():
    nome = input('Digite seu nome')
    email = input('digite seu e-mail')
    senha = input('digite sua senha')
    senha2 = input('Repita sua senha')

    return nome, email, senha, senha2

op = -1
while(op != 0):
    print('1-Cadastrar usuário')
    print('2-Login')
    print('0-Sair do programa')

    op = int(input('Digite a opçao desejada '))
    if(op == 1):
        nome, email, senha, senha2 =ler_info_usuario()

        while(verificar_user_existente(email, users)):
            email = input('digite novamente seu e-mail')

        while(verificar_senha(senha, senha2)):
            print('dessa vez digite senhas iguais')
            senha = input('digite sua senha')
            senha2 = input('Repita sua senha')

        novo_usuario = [nome, email, senha]
        inserir_usuario(novo_usuario, users)