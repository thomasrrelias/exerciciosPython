p = 0
s = 0
mu = 0 
while True:
     print('-' * 29)
     print('     CADASTRE UMA PESSOA')
     print('-' * 29)
     idade = int(input('Idade: '))
     if idade >= 18:
          p = p + 1
     sexo = ' '
     while sexo not in 'MF':
         sexo= str(input('Sexo:[M/F] ')).strip().upper()[0]
         if sexo == 'M':
              s = s + 1
     if sexo == 'F' and idade < 20:
          mu = mu + 1
     print('-' * 29)
     com = ' '
     while com not in 'SN':
          com = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
     if com == 'N':
          break
print ('-'*44)
print(f'Total de pessoas com mais de 18 anos: {p}')
print(f'Ao todo temos {s} homem cadastrado.')
print(f'Mulheres com menos de 20 anos: {mu}')