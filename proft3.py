
users = dict()

filmes = []
op = 99
opcliente = True
while(op != 0):

    print('-----------Menu-----------\n')
    print('1- Cadastrar Usuário')
    print('2- Comprar Ingressos')
    print('3- Gerenciar Filmes')
    print('0- Sair')


    op = int(input('\n Digite a opção desejada: '))
    if(op == 0):
        break
    if(op == 1):

        print('-----------Cadastro de usuário-----------\n')
        nome = input('Digite seu nome completo: ')
        email = input('Digite seu e-mail: ')
        usuario = input('Digite o nome de usuário: ')
        senha = input('Digite sua senha: ')
        escolha = input('Digite 1 se você for Administrador ou 2 se você for Cliente: ')
        users[nome] = [nome, email, senha, usuario, escolha]
        print('\n Cadastro efetuado com sucesso! \n')
        users = {'usuario':[usuario],'senha':[senha]}
        for item in users:
             if(item == 'usuario' and users[item][0] == senha ):
                print(item)
                print(users[item])
        #if(escolha == 1 or escolha == 2):
          #  print('\n Cadastro efetuado com sucesso! \n')
       # else:
         #   print('Você não digitou uma opção válida. Tente novamente!')



       # users = ()
       # for chave in users:
    #        if(chave == users and chave == email[1]):
          #      print('Usuário/e-mail já cadastrado. Tente fazer login ou insira outro usuário/e-mail!')

    if(op == 2):
        print('-----------Login Cliente-----------\n')
        user = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        if(user == dict [users]):
            print('Login efetuado com sucesso!\n')
        print('-----------Área do cliente-----------\n')
        print('-----------Menu cliente-----------\n')
        print('1- Ver filmes disponíveis')
        print('2- Comprar ingressos')
        print('3- Ver valores de ingressos')
        print('4- Ver horários das sessões disponíveis')
        print('0- sair')
        if(op == 0):
            break
        opcliente = input('\nDigite a opção desejada: \n')
        opcliente = 99
        if():

            print('Usuário/senha incorretos. Tente novamente! ')
        while(opcliente != 0):
            opcliente == False
            if(opcliente == 1):
                print(list[filmes])
            elif(opcliente == 2):
                ingressof = input('Digite o nome do filme: ')
            hora = input('Digite a opção de horário que você deseja: ')
            qtdeingressos = int(input('Digite a quantidade de ingressos que deseja: '))
            print(f'Você comprou {qtdeingressos} para o filme {ingressof} no horário {hora}.')
            confirmar = input('Digite SIM para confirmar e NÃO para cancelar compra: ')
            if(confirmar == 'SIM'):
                print('Compra realizada com sucesso. Bom filme :)')
            else:
                break
            if(op == 0):
                break

            elif(opcliente == 3):
                 print(list[valor])
            elif(opcliente == 4):
                print(list[horario])
            users = {'usuario': [usuario], 'senha': [senha]}
            for item in users:
                if (item == 'usuario' and users[item][1] == senha):
                    print(item)
                    print(users[item])





    if(op == 3):
      print('-----------Área login Administrador-----------\n')
      usuarioadm = input('Digite seu nome de usuário: ')
      senha = input('Digite sua senha: ')

      print('-----------Menu Administrador-----------\n')
      print('1- Realizar cadastro de filme')
      print('2- Buscar filme')
      print('3- Atualizar dados do filme')
      print('4- Remover filme')
      opcao = int(input('Digite a opção desejada: '))

      nome = input('Digite o nome do filme: ')
      sala = int(input('Digite a sala que será exibido o filme: '))
      horario = input('Digite o horário da sessão do filme: ')
      capacidade = int(input('Digite a capacidade da sala de exibição do filme: '))
      valor = float(input('Digite o valor do ingresso: '))
      sinopse = input('Digite um breve resumo sobre o filme: ')
      list.append(nome)
      list.append(sala)
      list.append(capacidade)
      list.append(valor)
      list.append(sinopse)

      busca = input('Digite o nome do filme que quer buscar: ')
      for nome in list(nome):
        if (nome.count(busca) > 0):
            print(nome)
        elif (opcao == 3):
            busca = input('Digite o nome do filme que quer atualizar: ')
        for i in range(len(list(nome))):
          if (list(nome)[i].count(busca) > 0):
              print(f'{i} - {list[i]}')
              atualizar = input('Digite o nome do filme que quer atualizar os dados: ')
              while (opcaoatt != 0):
                  print('1- Atualizar nome de filme')
                  print('2- Atualizar a sala que o filme será exibida')
                  print('3- Atualizar o horário de exibição do filme')
                  print('4- Atualizar a capacidade da sala de exibição do filme')
                  print('5- Atualizar valor do ingresso')
                  print('6- Atualizar texto referente a sinopse')
                  opcaoatt = int(input('Digite a opção desejada: '))
                  opcaoatt = -1
                  if (opcaoatt == 1):
                      novo_nome = input('Digite o novo nome do filme: ')
                      list(nome)[atualizar] = novo_nome
                  elif (opcaoatt == 2):
                      busca = list(sala)
                      for i in range(len(list(sala))):
                          if (list(sala)[i].count(busca) > 0):
                              print(f'{i} - {list(sala)[i]}')
                              novasala = int(input('Digite a nova sala: '))
                              list(sala)[atualizar] = novasala
                  elif (opcaoatt == 3):
                      busca = list(horario)
                      for i in range(len(list(horario))):
                          if (list(horario)[i].count(busca) > 0):
                              print(f'{i} - {list(horario)[i]}')
                              novohorario = input('Digite o novo horário de exibição do filme: ')
                              list(horario)[atualizar] = novohorario
                  elif (opcaoatt == 4):
                      busca = list(capacidade)
                      for i in range(len(list(capacidade))):
                          if (list(capacidade)[i].count(busca) > 0):
                              print(f'{i} - {list(capacidade)[i]}')
                              novacapacidade = int(input('Digite a nova capacidade da sala: '))
                              list(capacidade)[atualizar] = novacapacidade
                  elif (opcaoatt == 5):
                      busca = list(valor)
                      for i in range(len(list(valor))):
                          if (list(capacidade)[i].count(busca) > 0):
                              print(f'{i} - {list(valor)[i]}')
                              novovalor = float(input('Digite o novo valor do ingresso: '))
                              list(valor)[atualizar] = novovalor
                  elif (opcaoatt == 6):
                      busca = list(sinopse)
                      for i in range(len(list(sinopse))):
                          if (list(sinopse)[i].count(busca) > 0):
                              print(f'{i} - {list(sinopse)[i]}')
                              novasinopse = input('Digite a nova sinopse do filme: ')
                              list(sinopse)[atualizar] = novasinopse
