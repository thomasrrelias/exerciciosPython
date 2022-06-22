print('Aumento salarial.')
sa = float(input('Salario atual do funcionario: R$'))
aus = float(input('Porcentagem do aumento:'))
p = sa * (aus / 100)
rs = sa - p
print('O novo salario com reajuste de {:.0f}% é R${:.2f}'.format(aus, rs))
