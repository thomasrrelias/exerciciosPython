print('Toda loja com descontos')
vt = float(input('Valor do produto'))
d = float(input('Desconto do produto'))
vd = vt*(d / 100)
vf = vt - vd
print ('O valor do produto com {:.0f}% de desconto é R${:.2f}'.format(d, vf))
