print('Conversor de medida!')
mt = int(input('Digite a medida em metros: '))
km = mt / 1000
dm = mt * 10
cm = mt * 100
mm = mt * 1000
print('A medida corresponde a: \n{}km \n{}Dm \n{}Cm \n{}Mm'.format(km, dm, cm, mm))
