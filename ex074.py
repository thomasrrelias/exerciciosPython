from random import randint
from socket import NI_NUMERICHOST
nun = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in nun:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(nun)}')
print(f'O menor valor sorteado foi: {min(nun)}')
