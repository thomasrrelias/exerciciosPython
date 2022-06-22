lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidos', 4.20, 'Compasso', 9.90, 'Mochila', 120.30, 'Caneta', 3.70, 'livro', 34.90)
print('-'* 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'* 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end= '')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)