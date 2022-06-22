numero = int(input('Digite um numero inteiro: '))
print('Escolha uma base para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Conervter para HEXADECIMAL')
opç = int(input('Sua opção: '))
if opç == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif opç == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif opç == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção invadalida.')
