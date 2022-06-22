print('Aluguel de carro.')
print('-' * 20)
print('Diaria do carro R$60,00. \nPor km rodado R$0,15.')
print('-' * 20)
dia  = float(input('Quantos dias usou? '))
km = float(input('Quantos km rodou? '))
print('-' * 20)
vd = dia * 60.00
vkm = km * 0.15
vt = vkm + vd
print('Valor total das diarias: R${:.2f} \nValor total dos km: R${:.2f}'.format(vd, vkm))
print('=' * 20)
print('Valor total do aluguel: R${:.2f}'.format(vt))
