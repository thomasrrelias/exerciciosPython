num = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite umais um numero: ')), int(input('Digite o ultimo numero numero: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9  apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro 3 apareceu na {num.index(3)+1} posição')
else:
    print('O numero 3 nao apareceu.')
print('Os numeros pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
