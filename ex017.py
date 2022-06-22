import math
print('Descubra a hipotenusa do tringulo:')
n1 = float(input('Comprimento do cateto oposto: '))
n2= float(input(' Comprimnrto do cateto adjacente: '))
hip = math.hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
