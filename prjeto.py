users = {}
filmes = []
valor_ingressos = 25.70

while True:
    print('\n------Menu Principal------\n')
    print('1- Cadastrar Usuário')
    print('2- Gerenciar Filmes')
    print('3- Comprar Ingressos')
    print('0- Sair')

    opcmenuprin = int(input('Digite a opção desejada: '))

    if opcmenuprin == 1:
        nome = input('Digite seu nome completo: ')
        login = input('Digite seu login para cadastro: ')
        senha = input('Digite sua senha para cadastro: ')
        perfil = int(input('Digite 1 para Administrador e 2 para Cliente: '))
        users[login] = [nome, senha, perfil]
        print('Cadastro realizado com sucesso!\n')

    elif opcmenuprin == 2:
        login = input('Digite seu login para entrar: ')
        senha = input('Digite sua senha para entrar: ')
        logado = login in users and users[login][1] == senha

        if logado:
            print('\nLogin realizado com sucesso!\n')
            print('------Menu do Administrador------\n')
            print('1- Cadastrar Filme')
            print('2- Buscar Filmes')
            print('3- Atualizar Dados do Filme')
            print('4- Remover Filme')
            print('5- Mostrar Todos os Filmes Disponíveis')
            print('0- Logout')

            op = int(input('Digite a opção desejada:'))

            if op == 1:
                nomedofilme = input('Digite o nome do filme que deseja adicionar: ')
                ano = int(input('Digite o ano de lançamento do filme: '))
                diretor = input('Digite o nome do diretor do filme: ')
                horarios = input('Digite os horários de exibição do filme: ')
                valor = float(input('Digite o valor do ingresso: '))
                salas = input('Digite as salas que exibirão o filme: ')
                capacidade = input('Digite os lugares disponíveis na sala: ')
                filmes.append({"Nome do Filme": nomedofilme, "Ano de lançamento": ano, "Diretor": diretor, "Horários": horarios, "Valor do Ingresso": valor, "Salas": salas, "Capacidade": capacidade})
                print(f'O filme {nomedofilme} foi adicionado com sucesso!')

            elif op == 2:
                busca = input('Digite o filme que deseja buscar: ')
                for filme in filmes:
                    if busca in filme.values():
                        print(filme)

            elif op == 3:
                busca = input('Digite o nome do filme que deseja atualizar: ')
                for i, filme in enumerate(filmes):
                    if busca in filme.values():
                        print(f'{i} - {filme}')
                        cod = int(input('Digite o código do que deseja atualizar: '))
                        print('\nFilme Atualizado Com Sucesso!\n')

            elif op == 4:
                busca = input('Digite o nome do filme que deseja remover: ')
                for i, filme in enumerate(filmes):
                    if busca in filme.values():
                        del filmes[i]
                        print(f'O filme {busca} foi removido com sucesso!')
                        break

            elif op == 5:
                for t in filmes:
                    print(t)

            elif op == 0:
                break

        else:
            print('Usuário ou senha inválidos, tente novamente!')

    elif opcmenuprin == 3:
        login = input('Digite seu login para entrar: ')
        senha = input('Digite sua senha para entrar: ')
        logado = login in users and users[login][1] == senha

        if logado:
            print('\nLogin realizado com sucesso!\n')
            print('\n------Menu do Cliente------\n')
            print('1- Comprar ingressos')
            print('2- Ver filmes disponíveis')
            print('3- Sair')
            opccliente = int(input('Digite a opção desejada: '))

            if opccliente == 1:
                qtde = int(input('Digite a quantidade de ingressos que deseja comprar: '))
                escolhafilme = input('Digite o filme que deseja assistir: ')
                escolhasala = int(input('Digite a sala que deseja assistir: '))
                escolhahorario = input('Digite o horário da sessão que deseja comprar o ingresso: ')
                escolhalugar = int(input('Digite a numeração da cadeira onde deseja assistir o filme: '))
                total = qtde * valor_ingressos
                print(f'Sua compra total foi de R$: {total}. Obrigado pela preferência e volte sempre :)!')

            elif opccliente == 2:
                for f in filmes:
                    print(f)

            elif opccliente == 3:
                break

    elif opcmenuprin == 0:
        break