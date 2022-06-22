from random import randint
computador = randint(0, 5)
print( 20 * '-=-')
print('Pensei em um numero de 0 a 5, tente adivinhar....')
print( 20 * '-=-')
jogador = int(input('Em que numero eu pensei???'))
if jogador == computador:
    print ('Parabens você acertou!!!')
else:
    print ('Não foi dessa vez!!! O numero que pensei foi {}'.format(computador))
    
              
