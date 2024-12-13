print('\n-----Cine Sertão-----\n')
filmes = list()

login = {}
op = 99

while(op != 0):

    print('--------Menu--------')
    print('1- Cadastro de Usuário')
    print('2- Comprar de Ingressos')
    print('3- Gerenciar Filmes')
    print('0- Sair')
    op = int(input('\nDigite a opção desejada: '))

    if(op == 1):
        print('\n-----Cadastro de Usuário-----\n')
        nome = input('Digite seu nome completo: ')
        email = input('Digite seu e-mail: ')
        user = input('Dirio: ')
        senha = input('Digite umagite um nome de usuá senha: ')
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
              print('5- Comprar ingressos')
              opcliente = int(input('Digite a opção desejada'))
              if (opcliente == 1):
               for f in filmes:
                  print(f)

          else:
              print('Usuário ou senha inválidos. Tente novamente! ')


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
            print('1-Cadastrar Filme')
            print('2- Buscar Filmes')
            print('3- Atualizar dados do filme')
            print('4- Remover filme')
            print('5- Mostrar todos os filmes')
            print('0- Sair')
            opcadm = int(input('Digite a opção desejada: '))
            if(opcadm == 1):
                nome = input('Digite o nome do filme: ')
                ano = input('Digite o ano que foi lançado: ')
                diretor = input('Digite o nome do diretor: ')
                horario = input('Digite os horários das sessões desse filme: ')
                valor = float(input('Digite o valor do ingresso: '))
                sala = int(input('Digite as salas que irão exibir esse filme: '))
                filmes.append(nome)
                filmes.append(ano)
                filmes.append(diretor)
                filmes.append(horario)
                filmes.append(valor)
                filmes.append(sala)
            elif(opcadm ==2):
                busca = input('Digite o nome do filme que deseja buscar: ')
                for i in filmes:
                    if(busca in filmes):
                        print(filmes)
            elif(opcadm == 3):
                busca = int(input('Digite o nome do filme que deseja atualizar: '))
                for a in filmes:
                    if(busca in filmes):
                        print('1- Para atualizar o nome do filme')
                        print('2- Para atualizar horários do filme')
                        print('3- Para atualizar preço dos ingressos')
                        print('4- Para atualizar salas de exibição do filme')
                        print('5- Para atualizar lugares disponíveis')

                        opcadm = int(input('Digite a opção desejada: '))
                        if(opcadm == 1):
                            for filme in filmes:
                                if(busca in filmes):
                                    novonome = input('Digite o novo nome do filme: ')
                                    filme[filmes] = novonome