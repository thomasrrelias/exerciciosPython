velocidade = float(input('Qual a velocidade atual do carro?'))
multa = (velocidade-80) * 7
if velocidade <= 80:
    print('Tenha uma boa tarde! Dirija com cuidado!')
else:
    print ('MULTADO! Você excedeu o limite permitido de 80km/h')
    print ('Valor por km/h excedico: R$7,00')
    exedido = (velocidade - 80)
    print ('km/h excedida: {}km/h'.format(exedido))
    print ('--'*20)
    print ('Valor total a pagar: R${}'.format(multa))
       
