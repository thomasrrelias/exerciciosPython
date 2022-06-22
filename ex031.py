print ('Preço de viagem!')
km = float(input('Quantos km é a viagem: '))
if km <= 200:
    print('ORÇAMENTO:')
    print('--'*20)
    print('Valor por Km baixo de 200Km: R$0,50')
    valor1 = km * 0.5
    print('Valor total: R${}'.format(valor1))
    print('--'*20)
else:
    print('ORÇAMENTO:')
    print('--'*20)
    print('Valor por Km acima de 200Km: R$0,40')
    valor2 = km * 0.4
    print('Valor total: R${}'.format(valor2))
    print('--'*20)
