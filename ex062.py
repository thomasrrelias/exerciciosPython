print('Gerador de PA')
print ('=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print('{} -> '.format(termo),  end='')
        cont = cont + 1
        termo = termo + razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão final com {} termos mostrados.'.format(total))

