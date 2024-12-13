print('\n-----Cine Sertão-----')
filme1 = {'Título': 'Planeta dos Macacos: O Reinado',
          'Ano': 2024,
          'Diretor': 'Wes Ball'}
filme2 = {'Título': 'Simplesmente Acontece',
          'Ano': 2014,
          'Diretor': 'Christian Ditter'}
filme3 = {'Título': 'Como Eu Era Antes de Você',
          'Ano': 2016,
          'Diretora': 'Thea Sharrock'}
filmes = []
filmes.append(filme1)
filmes.append(filme2)
filmes.append(filme3)

cliente = {}
login = list()
op = 99

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


        senha = input('Digite uma senha: ')
        #1
        # perfil = int(input('Digite 1 se for Administrador ou 2 se for Cliente: '))

        cadastrado = False
        for coch in cliente:
            if(coch == nome and cliente[nome][2] == senha):
                cadastrado = True



            print('\nCadastro efetuado com sucesso!')
        if(cadastrado):
            print('cadastro realizado com sucesso')
            print('~~~aba do adm~~~')
            print('1-cadastro de filme')
            print('2-filme')
            print('3-filme')
            print('0-sair do loguin')
        else:
            print('loguin de cliente invalido')

    elif(op == 2
    ):
        print('-----Área login do Administrador-----')
        user = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')


        cadastrado = False
        for coch in cliente:
            if(coch == nome and cliente[nome][2] == senha):
                cadastrado = True

            if(cadastrado):
                print('cliente cadastrado com sucesso')
                print('~~~~menu de cliente~~~~')

    elif(perfil == 3
    ):
          print('-----Área de login Cliente----- ')
          dict = {'user 1': 'victoriak',
                 'senha 1': '123456'
                  }
          user = input('Digite seu nome de usuário: ')
          senha = input('Digite sua senha: ')
          print('\n Login efetuado com sucesso!\n')
          print('\n-----Área do Cliente-----\n')
          print('\n-----Menu Cliente-----\n')
          print('1- Ver filmes disponíveis')
          print('2- Ver horários disponíveis')
          print('3- Ver valores de ingressos')
          print('4- Ver lugares disponíveis')
          print('5- Comprar ingressos')
          print('0- sair')
          opcliente = int(input('Digite a opção desejada'))
          if (opcliente == 1):
              for f in filmes:
                  print(f)





          else:
            print('Você está cadastrado como Administrador, faça login na área de admins.')


   # if(op == 3):
       # print('-----Área login do Administrador-----')
        #@user = input('Digite seu nome de usuário: ')
        #se#nha = input('Digite sua senha: ')


        #cadastrado = False
        #for coch in cliente:
         #   if(coch == nome and cliente[nome][2] == senha):
          #      cadastrado = True

            #if(cadastrado):
              #  print('cliente cadastrado com sucesso')
               # print('~~~~menu de cliente~~~~')