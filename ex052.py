numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1
print('O numero {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
        
    
