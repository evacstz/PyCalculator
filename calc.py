x = ''

while x != '0':
    print('''
          --------CALCULADORA--------
          Escolha uma operação:
          1 - Soma
          2 - Subtração
          3 - Multiplicação
          4 - Divisão
          5 - Elevar ao quadrado
          0 - Sair
          ---------------------------
          ''')
    x = input("")

    if x == '0':
        print('tchau tchau🫡')
        break

    if x == '1':
        print('Você escolheu soma.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print(f'{n1} + {n2} = {n1 + n2}')

    elif x == '2':
        print('Você escolheu subtração.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print(f'{n1} - {n2} = {n1 - n2}')

    elif x == '3':
        print('Você escolheu multiplicação.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print(f'{n1} * {n2} = {n1 * n2}')

    elif x == '4':
        print('Você escolheu divisão.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print(f'{n1} / {n2} = {n1 / n2}')

    elif x == '5':
        print('Você escolheu elevar ao quadrado.')
        n1 = int(input("Número: "))
        print(f'{n1}² = {n1 ** 2}')

    else:
        print('Erro, tente novamente...')