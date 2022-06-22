print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)
caro = valor = menor = cont =0
bara = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont = cont + 1
    if preço >= 1000:
        caro = caro + 1
    if cont == 1:
        menor = preço
        bara = nome
    else:
        if preço < menor:
            menor = preço 
            bara = nome
    valor = valor + preço 
    con = ' '
    while con not in 'SN': 
        con = str(input('Mais produtos? [S/N] ')).upper().strip()[0]
    if con == 'N':
        break
print('----------- FIM DAS COMPRAS -----------')
print(f'Total da compra: R$ {valor:.2f}')
print(f'temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {bara} custando R${menor:.2f}')