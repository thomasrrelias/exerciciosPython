frase = str(input('Digite uma frase: ')).strip()
frase2 = frase.upper()
print('A letra A aparece {} vezes na frase.'.format(frase2.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase2.find('A') + 1))
print('A letra A apareceu por ultimo na posição {}.'.format(frase2.rfind('A') + 1))
            
