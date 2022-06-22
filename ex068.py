from random import randint
print('=-'* 13)
print('VAMOS JOGAR PAR OU IMPAR!')
print("=-"*13)
v = 0
while True:
    valor = int(input('Digite um valor: '))
    comp = randint(0,10)
    total = valor + comp
    poi = ' '
    while poi not in 'PI':
        poi= str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        print('--'* 13)
    print(f'Você jogou {valor} e o computador jogou {comp}. Total de {total}.', end= ' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    print('--'*13)
    if poi == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v = v + 1
            print('Vamos jogar novamente...')
            print('=-='*30)
        else:
            print ('Você PERDEU!')
            break
    elif poi == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v = v + 1
            print('Vamos jogar novamente...')
            print('=-'*13)
        else:
            print ('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {v} vezes.')
