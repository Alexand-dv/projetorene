print('\n-----Cine Sertão-----\n')
filmes = = {1:['Título': {'Planeta dos Macacos',: 100','Ano': 2024, 'Wes Ball'}],
            2:['Título 1': {'Simplesmente Acontece:Ano' 2014,Christian Ditter}],
            3:['Título 2': {'Como Eu Era Antes de Você','Ano': 2016,'Diretora': 'Thea Sharrock'}],
}


hora0 = {'Horário': '16:00'}
hora1 = {'Horário': '18:00'}
hora2 = {'Horário': '20:00'}
horarios = []
horarios.append(hora0)
horarios.append(hora1)
horarios.append(hora2)

valor0 = {'Ingresso Meia': 35.00}
valor1 = {'Ingresso Inteiro': 70.00}
valores = []
valores.append(valor0)
valores.append(valor1)

lugar0 = {'Sala 1': 'Lugares: 09, 16, 24, 38'}
lugar1 = {'Sala 2': 'Lugares: 07, 13, 17, 18, 19, 21'}
lugar2 = {'Sala 3': 'Lugares: 01, 03, 04, 07, 09, 10, 14, 18, 20,'}
lugares = []
lugares.append(lugar0)
lugares.append(lugar1)
lugares.append(lugar2)


login = {}
op = 99
vl_ingresso = 35
max_ingre = 80

while(op != 0):

    print('-----Menu Principal-----')
    print('1- Cadastro de Usuário')
    print('2- Comprar de Ingressos')
    print('3- Gerenciar Filmes')
    print('0- Sair')
    op = int(input('\nDigite a opção desejada: '))

    if(op == 1):
        print('\n-----Cadastro de Usuário-----\n')
        nome = input('Digite seu nome completo: ')
        email = input('Digite seu e-mail: ')
        user = input('Digite um nome de usuário: ')
        senha = input('Digite uma senha: ')
        perfil = int(input('Digite 1 se for Administrador ou 2 se for Cliente: '))
        login[user] = [nome, email, senha, perfil]
        print('\nCadastro efetuado com sucesso!\n')
    elif(op == 2):
          print('\n-----Área de login Cliente----- \n')
          user = input('Digite seu nome de usuário: ')
          senha = input('Digite sua senha: ')

          logado = False
          for chave in login:
              if(chave == user and login[user][2] == senha):
                  logado = True
          if(logado):
             print('\n Login efetuado com sucesso!\n')
             print('\n-----Menu Cliente-----\n')
             print('1- Ver filmes disponíveis')
             print('2- Ver horários disponíveis')
             print('3- Ver valores de ingressos')
             print('4- Ver lugares disponíveis')
             print('5- Comprar ingressos')
             opcliente = int(input('Digite a opção desejada'))
             if (opcliente == 1):
               for f in filmes:
                  print(f)
             elif(opcliente == 2):
                 for h in horarios:
                     print(h)
             elif(opcliente == 3):
                 for v in valores:
                     print(v)
             elif(opcliente == 4):
                 for l in lugares:
                     print(l)
                 else:
                     print('Usuário ou senha inválidos. Tente novamente! ')
             elif(opcliente == 5):

                qde_ingresso = int(input('diigite a quantidade de ingresso que dejesa comprar'))


                vl_ingresso *= qde_ingresso


                print(f'  valor R$ {vl_ingresso}')


    elif(op == 3):
        print('-----Área login do Administrador-----')
        user = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')

        logado = False
        for chave in login:
            if(chave == user and login[user][2] == senha):
                logado = True
        if(logado):
            print('\nLogin realizado com sucesso.')
            print('-----Menu Administrador-----')
            print('1 -Cadastrar Filme')
            print('2- Buscar Filmes')
            print('3- Atualizar dados do filme')
            print('4- Remover filme')
            print('0- Sair')
            opcadm = int(input('Digite a opção desejada: '))
            if(opcadm == 1):
                print('\n~~~~~~cadasto de filme~~~~')
                codigo = int(input('Digite o código do filme: '))
                nome = input('Digite o nome do filme: ')
                ano = input('Digite o ano que foi lançado: ')
                diretor = input('Digite o nome do diretor: ')
                filmes[codigo] = [nome, ano, diretor]
            elif(opcadm == 2):
                cod = int(input('digite o cod do filme que '))
                for chave in filmes:
                    if(filmes[chave][1][2]):
                        print(filmes[0])
