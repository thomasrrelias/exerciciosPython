from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10')
palpite  = 0
acertou = False
while not acertou:
    jogador = int(input('qual é o seu palpite? '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ('Mais... tente mais uma vez.')
        elif jogador > computador:
            print ('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. PARABENS!'.format(palpite))
