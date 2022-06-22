from itertools import count


print('Estude a tabuada!')
answer = 'sim'
while answer == 'sim':
    n = int(input('Digite um numero para ver sua tabuada: '))

    for count in range(0,11):
        print('{} x {} = {}'.format(n, count, n*count))

    print('-' * 12)
    answer = input('Quer fazer outra tabuada? ')
    print('Ok então, obg!')
