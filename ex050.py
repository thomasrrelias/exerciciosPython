soma = 0
cont = 0
print('Digite 6 valores inteiros:')
for c in range(1, 7):
    numero= int(input('Digite o {} valor: '.format(c)))
    if numero % 2 == 0:
        cont = cont + 1
        soma = soma + numero
print ('A soma dos seus {} numeros pares são {}.'.format(cont, soma))
        
