print('--=' * 20)
print('Vou pensar em um numero interio entre 0 e 5. Tente adivinhar...')
print('--=' * 20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO....')
if numero == 3:
    print('PARABÉNS!! Você ganhou!')
else:
    print('Eu ganhei! Pensei no numero 3 e não no {}!'.format(numero))
    
    
