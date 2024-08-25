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
    x = input("Opção: ")

    if x == '0':
        print('tchau tchau🫡')
        break

    if x == '1':
        print('Você escolheu soma.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')

    elif x == '2':
        print('Você escolheu subtração.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        sb = n1 - n2
        print(f'{n1} - {n2} = {sb}')

    elif x == '3':
        print('Você escolheu multiplicação.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        m = n1 * n2
        print(f'{n1} * {n2} = {m}')

    elif x == '4':
        print('Você escolheu divisão.')
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        d = n1 / n2
        print(f'{n1} / {n2} = {d}')

    elif x == '5':
        print('Você escolheu elevar ao quadrado.')
        n1 = int(input("Número: "))
        p = n1 ** 2
        print(f'{n1}² = {p}')

    elif x != ['0', '1', '2', '3', '4', '5']:
        print('Erro, tente novamente...')