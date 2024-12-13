users = {}
filmes = list()
opcmenuprin = 99

while(opcmenuprin != 0):
    print('\n------Menu Principal------\n')
    print('1- Cadastrar Usuário')
    print('2- Gerenciar Filmes')
    print('3- Comprar Ingressos')
    print('0- Sair')

    opcmenuprin = int(input('Digite a opção desejada: '))

    if(opcmenuprin == 1):
        print('------\nCadastro de Usuário------\n')
        nome = input('Digite seu nome completo: ')
        login = input('Digite seu login para cadastro: ')
        senha = input('Digite sua senha para cadastro: ')
        perfil = int(input('Digite 1 para Administrador e 2 para Cliente: '))

        users[login] = [nome, senha, perfil]
        print('Cadastro realizado com sucesso!\n')

    elif(opcmenuprin == 2):
        login = input('Digite seu login para entrar: ')
        senha = input('Digite sua senha para entrar: ')

        logado = False
        for chave in users:
            if(chave == login and users[login][1] == senha):
                logado = True


        if(logado ):
            print('\n Login realizado com sucesso! \n')
            print('------Menu do Administrador------\n')
            print('1- Cadastrar Filme')
            print('2- Buscar Filmes')
            print('3- Atualizar Dados do Filme')
            print('4- Remover Filme')
            print('5- Mostrar Todos os Filmes Disponíveis')
            print('0- Logout')
            op = int(input('Digite a opção desejada: '))
            if(opcmenuprin == 3):
                for i in range(4):
                    nomefil = input('digite o nome do filme')
                    nomdiretor = input('digite o onme do diretor1')
                    ano = (input('digite o ano do filme'))
                    filmes.append({'nome': nomefil, 'valor': nomdiretor, 'val': ano})

                print('\nMENU de filmes\n')
                for prod in filmes:
                    print(prod['nome'])

                film_patualiz = input('digite o nome do produto que vc deseja atualizar o preco')
                for i in range(len(filmes)):
                    if (filmes[i]['nome'] == film_patualiz):
                        novoP = input('digite o novo film')
                        filmes[i]['valor'] = film_patualiz

                for p in filmes:
                    print(p)

            if(op == 1):
                for i in range():
                    nomefilme = input('Digite o nome do filme: ')
                   # ano = int(input('Digite o ano de lançamento do filme: '))
                    diretor = input('Digite o nome do diretor do filme: ')
                    horarios = input('Digite os horários de exibição do filme')
                    valor = float(input('Digite o valor do ingresso: '))
                    salas = input('Digite as salas que exibirão o filme: ')
                    capacidade = input('Digite os lugares disponíveis na sala: ')

                    filmes.append(nomefilme)
                    filmes.append(ano)
                    filmes.append(diretor)
                    filmes.append(horarios)
                    filmes.append(valor)
                    filmes.append(salas)
                    filmes.append(capacidade)


            elif(op == 2):

                busca = input('Digite o filme que deseja buscar: ')
                for filme in filmes:
                    if(busca in filmes ):
                        print(filme)


            elif(op == 5):
                for nome in filmes:
                    print(nome)



            else:
             print('Usuário ou senha inválidos, tente novamente!')


    elif(opcmenuprin == 3):
        login= input('Digite seu login para entrar: ')
        senha = input('Digite sua senha para entrar: ')

        logado = False

        for chave in users:
            if (chave == login and users[login][1] == senha):

                    logado = True




        if(logado):
            print('\n Login realizado com sucesso! \n')
            print('\n ------Menu do Cliente------\n')
            print('1- Comprar ingressos')
            print('2- Ver filmes disponíveis')
            print('3- Sair')
            opccliente = int(input('Digite a opção desejada: '))


            if(opccliente == 1):
                qtde = int(input('Digite a quantidade de ingressos que deseja comprar: '))
                escolhafilme = input('Digite o filme que deseja assistir: ')
                escolhasala = int(input('Digite a sala que deseja assistir: '))
                escolhahorario = input('Digite o horário da sessão que deseja comprar o ingresso: ')
                escolhalugar = int(input('Digite a numeração da cadeira onde deseja assistir o filme: '))
                finalizar = input('Digite Sim para CONFIRMAR a compra. E Não para CANCELAR a compra.')
                valoringresso = 25.70
                total = qtde * valoringresso

                print(f' Sua compra total foi de R$: {total}. Obrigado pela preferência e volte sempre :)!')


            elif(opccliente == 2):
                for f in filmes:
                    print(f)


            elif(opccliente == 3):

                break



