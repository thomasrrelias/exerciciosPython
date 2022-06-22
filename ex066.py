cont = som = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont = cont + 1
    som = som + num
print (f'A soma de {cont} valores foi de {som}!')
