n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('=-=' * 20)
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        print('=-=' * 20)
    elif op == 3:
        if n1 < n2:
            print('{} é o maior numero.'.format(n2))
        elif n1 > n2:
            print('{} é o maior numero.'.format(n1))
        else:
            print('Os numeros são iguais.')
        print('=-=' * 20)
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 4:
        print('Informe os numeros de novo:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 20)
    elif op == 5:
       print('Finalizando....') 
    else:
        print('Opção invalida! Tente novamente:')
print('FIM do programa! Volte sempre!') 
         
