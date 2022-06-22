print('Aumento salarial:')
salario = float(input('Qual o salario atual: '))
if salario <= 1250.0:
    print('O salario atual é: {:.2f}'.format(salario +(salario * 0.15)))
else:
    print('O salario atual é: {:.2f}'.format(salario + (salario * 0.10)))
