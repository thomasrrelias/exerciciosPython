somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).title().strip()
    somaidade = somaidade + idade
    if p == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher = totmulher + 1
mediaidade = somaidade/ 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
