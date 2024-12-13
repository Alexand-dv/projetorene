
usuarios = []
eventos = []
certificado = []
def vericar_senha(senha1, senha2):
    if(senha1 != senha2):
        return True
    else:
        return False
def vericar_event(event,event2):
    if(event != event2):
        return True
    else:
        return False

def verificar_usuarios_exixtentes(email, usuarios):
    existente = False
    for usuario in usuarios:
        if(usuario[1] == email):
            existente = True
            break
        return existente
def verificar_eventoso_exixtentes(nomedoevento, eventos):
    existente = False
    for evento in eventos:
        if(evento[0] == nomedoevento):
            existente = True
            break
        return existente
def adicionar_usuarios(usuario, lista_usuarios):
    lista_usuarios.append(usuario)
def adicionar_evento(evento, lista_eventos):
    lista_eventos.append(evento)


def verificar_informacoes_cadastrado():
    nome = input('digite seu nome')
    email = input('digite seu email')
    senha = input('digite sua senha')
    senha2 = input('digite novamente sua senha')
    return nome, email, senha, senha2
def verificar_informacoes_cadastrado_evento():
    nomedoevento = input('digite o nome do evento')
    val_inscricao = input('digite o valor da inscricao')
    event = input('digite sua senha')
    event2 = input('digite novamente sua senha')

    return nomedoevento, val_inscricao, event, event2
op = -1
while(op != 0):
    print('----- MENU PRINCIPAL -----')
    print('1 - CADASTRO DE USUÁRIO')
    print('2 - LOGIN')
    print('0  -SAIR')

    op = int(input('Digite uma das opções solicitadas: '))
    if(op == 1):

        nome, email, senha, senha2 = verificar_informacoes_cadastrado()

        while(verificar_usuarios_exixtentes(email, usuarios)):
            email = input('Digite seu email corretamente por favor!')
        while (vericar_senha(senha, senha2)):
            print('Digite a senha correta!')
            senha = input('Digite sua senha: ')
            senha2 = input('Digite novamente sua senha: ')

            novo_usuario = [nome, email, senha]
            adicionar_usuarios(novo_usuario)
            print (usuarios)
    elif(op == 2):
        print('\n----- ÁREA DE CADASTRO ----- \n')
        usuario = input('Digite seu nome de usuário: ')
        senha2 = input('Digite sua senha: ')
        logado = False
        if usuario in usuarios:
            ind1 = -1
            ind2 = -1
            for i in range(len(usuarios)):
                if (usuarios [i][0] == usuario):
                    ind1 = i
                    for i in range(len(usuarios)):
                        if (usuarios[i][2] == senha2):
                            ind2 = i
                            for chave in usuarios:
                                if (chave == usuarios[ind1][0] and chave == usuarios[ind2][2]):
                                    logado = True

                            if (logado == True):
                                print('\n LOGIN EFETUADO COM SUCESSO\n')
                                print('\n----- MENU CLIENTE -----\n')
                                print('1 - CADASTRO DE EVENTO')
                                print('2 - BUSCAR EVENTO')
                                print('3 - LISTAR EVENTOS')
                                print('4 - REMOVER EVENTO')
                                print('5 - INSCRIÇÃO EVENTO')

                                opcaopevento = int(input('Digite a opção desejada'))
                                if(opcaopevento == 1):
                                    for e in evento:
                                        print(e)
                                elif(opcaopevento == 2):
                                    for horario in evento:
                                        print(horario)

    elif(op == 3):
        novo_usuario, val_inscricao = verificar_informacoes_cadastrado_evento()
        print('\n -------area de cadastro de evento------- \n')
        while (verificar_eventoso_exixtentes(nomedoevento, evento)):
            nomedoevento = input('digite o nome do evento')

        while (vericar_event(event, event2)):
            print('digite a senha correta')
            event = input('digite sua senha')
            event2 = input('digite novamente sua senha')
            nomedoevento = input('digite o nome do evento')




            nov_evento = [nomedoevento, val_inscricao]
            adicionar_evento(nov_evento, evento)

            print(nov_evento)








            print('2- Ver horários de eventos')
            print('3- Ver valor da inscricao')
            print('4- Ver vagas disponiveis')
            print('5- pagar inscricao')