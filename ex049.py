numero = int(input('Digite um numero para ver sua tabuada: '))
for c in range(0, 11):
    numero1 = numero * c
    print('{} x {} = {}'.format(numero, c, numero1))
