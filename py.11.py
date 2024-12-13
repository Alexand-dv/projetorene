users = dict()
filmes = []
op = 99

while(op != 0):

    print('-----------Menu-----------\n')
    print('1- Cadastrar Usuário')
    print('2- Comprar Ingressos')
    print('3- Gerenciar Filmes')
    print('0- Sair')

    op = int(input('\n Digite a opção desejada: '))
    if(op == 1):
        nome = input('Digite seu nome completo:')
        email = input('Digite seu e-mail: ')
        user = input('Digite o nome de usuário: ')
        senha = input('Digite sua senha: ')
        escolha = input('Digite 1 se você for Administrador ou 2 se você for Cliente: ')




        users[user] = [nome, email, senha, user, escolha,]
        print('\n cadastro efetuado com sucesso! \n')
    #elif(user != user):
       # print('Usuário inválido. Digite novamente.')
    #elif(senha != senha):
        #print('Senha inválida. Digite novamente.')
    if(escolha != 2 or escolha !=1):
        print('voce nao digitou opcao valida')


        user = ()
        for chave in users:
            if(chave == user and chave == email[1]):
                print('usuarui ou email ja cadastrado')




        opcao = 99
        while(opcao != 0):
            if(escolha == 1):
                usuarioadm = input('Digite seu nome de usuário: ')
                senha = input('Digite sua senha: ')

                print('1- Realizar cadastro de filme')
                print('2- Buscar filme')
                print('3- Atualizar dados do filme')
                print('4- Remover filme')
            opcao = int(input('Digite a opção desejada: '))
            if(opcao == 1):
                nome = input('Digite seu nome completo:')
                email = input('Digite seu e-mail: ')
                user = input('Digite o nome de usuário: ')
                escolha = input('Digite 1 se você for Administrador ou 2 se você for Cliente: ')

            if (op == 2):
                usuario = input('Digite seu nome de usuário: ')
                senha = input('Digite sua senha: ')
                print('\n Login efetuado com sucesso!\n')












            elif(opcao == 3):
                nome = input('Digite o nome do filme: ')
                sala = int(input('Digite a sala que será exibido o filme: '))
                horario = input('Digite o horário da sessão do filme: ')
                capacidade = int(input('Digite a capacidade da sala de exibição do filme: '))
                valor = float(input('Digite o valor do ingresso: '))
                sinopse = input('Digite um breve resumo sobre o filme: ')
                list.append(nome)
                list.append(sala)
                list.append(horario)
                list.append(capacidade)
                list.append(valor)
                list.append(sinopse)

                busca = input('Digite o nome do filme que quer buscar: ')
                for nome in list(nome):
                    if(nome.count(busca) > 0):
                        print(nome)
            elif(opcao == 3):
                busca = input('Digite o nome do filme que quer atualizar: ')
                for i in range(len(list(nome))):
                    if(list(nome)[i].count(busca) > 0):
                        print(f'{i} - {list[i]}')
                        atualizar = input('Digite o nome do filme que quer atualizar os dados: ')
                        while(opcaoatt != 0):
                            print('1- Atualizar nome de filme')
                            print('2- Atualizar a sala que o filme será exibida')
                            print('3- Atualizar o horário de exibição do filme')
                            print('4- Atualizar a capacidade da sala de exibição do filme')
                            print('5- Atualizar valor do ingresso')
                            print('6- Atualizar texto referente a sinopse')
                            opcaoatt = int(input('Digite a opção desejada: '))
                            opcaoatt = -1
                            if(opcaoatt == 1):
                                novo_nome = input('Digite o novo nome do filme: ')
                                list(nome)[atualizar] = novo_nome
                            elif(opcaoatt == 2):
                                busca = list(sala)
                                for i in range(len(list(sala))):
                                    if(list(sala)[i].count(busca) > 0):
                                        print(f'{i} - {list(sala)[i]}')
                                        novasala= int(input('Digite a nova sala: '))
                                        list(sala)[atualizar] = novasala
                            elif(opcaoatt == 3):
                                busca = list(horario)
                                for i in  range(len(list(horario))):
                                    if(list(horario)[i].count(busca) > 0):
                                        print(f'{i} - {list(horario)[i]}')
                                        novohorario = input('Digite o novo horário de exibição do filme: ')
                                        list(horario)[atualizar] = novohorario
                            elif(opcaoatt == 4):
                                busca = list(capacidade)
                                for i in range(len(list(capacidade))):
                                    if(list(capacidade)[i].count(busca) > 0):
                                        print(f'{i} - {list(capacidade)[i]}')
                                        novacapacidade = int(input('Digite a nova capacidade da sala: '))
                                        list(capacidade)[atualizar] = novacapacidade
                            elif(opcaoatt == 5):
                                busca = list(valor)
                                for i in range(len(list(valor))):
                                    if(list(capacidade)[i].count(busca) > 0):
                                        print(f'{i} - {list(valor)[i]}')
                                        novovalor = float(input('Digite o novo valor do ingresso: '))
                                        list(valor)[atualizar] = novovalor
                            elif(opcaoatt == 6):
                                busca = list(sinopse)
                                for i in range(len(list(sinopse))):
                                    if(list(sinopse) [i].count(busca) > 0):
                                        print(f'{i} - {list(sinopse)[i]}')
                                        novasinopse= input('Digite a nova sinopse do filme: ')
                                        list(sinopse)[atualizar] = novasinopse
    if(op == 2):
        usuario = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        print('\n Login efetuado com sucesso!\n')
    if(op == 3):
        nome = input('Digite seu nome completo:')
        email = input('Digite seu e-mail: ')
        user = input('Digite o nome de usuário: ')
        escolha = input('Digite 1 se você for Administrador ou 2 se você for Cliente: ')



