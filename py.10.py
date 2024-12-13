num1 = float(input('digite um numero'))
num2 = float(input('digite outro numero'))

if(num1 > num2):
    print(f'o numero {num1} e o maior')
if(num2 > num1):
    print(f'o numero {num2} e o maior')
if(num1 == num2):
    print('os dois numeros sao iguais')



    pessoas = {'felipe': 'maria', 'popo': 'penelope', 'jose': 'nyvi'}

    busca = input('digite o nome do cidadao')

    for pessoa in pessoas:
        if (busca in pessoa):
            novoamor = input('digite o nome do novo amor desta pessoa')
            pessoas[pessoa] = novoamor

    print(pessoas)