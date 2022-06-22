print('APROVAÇÃO para parcelamento de imovel imedito!')
print('Leia atentamente as condições!')
print('==' * 30)
print('Para o parcelamento ser aprovado\nimediatamente o valor das\nprestações não devem ser superiores\na 30% do valor salarial.')
print('==' * 30)
condiçoes = str(input('ESTÁ DE ACORDO COM AS CONDIÇÕES? ')).title().strip()
if condiçoes in 'Nao Não':
    print('OK! Obrigado pela atenção')
elif condiçoes == 'Sim':
    condiçoes = 'Sim'
    while condiçoes == 'Sim':
        valor = float(input('Valor do imovel: R$'))
        parc = float(input('Anos de parcelamento: '))
        sala = float(input('Salário atual: R$'))
        prest = valor / (parc*12)
        porc = sala * 0.3
        porcer = (prest / sala) * 100
        print('Para parcelar uma casa de R${:.2f} em {} anos '.format(valor, parc), end=' ')
        print('a prestação será de R${:.2f}'.format(prest))
        if prest <= porc:
            print('Parcelamento APROVADO!')
            condiçoes = str(input('Quer fazer outro parcelamento? ')).title().strip()
        elif condiçoes:
            print('Parcelamento NEGADO!\n{:.1f}% do salário, LEIA atentamente as condições!'.format(porcer))
            print('==' * 30)
            print('Para o parcelamento ser aprovado\nimediatamente o valor das\nprestações não devem ser superiores\na 30% do valor salarial.')
            print('==' * 30)
            condiçoes = str(input('Quer refazer?')).title().strip()
else:
    condiçoes = str (input('Não entendi! Digite de novo por favor:')).title().strip()
    if condiçoes in 'Nao Não':

        print('OK! Obrigado pela atenção')
    elif condiçoes == 'Sim':
        condiçoes = 'Sim'
        while condiçoes == 'Sim':
            valor = float(input('Valor do imovel: R$'))
            parc = float(input('Anos de parcelamento: '))
            sala = float(input('Salário atual: R$'))
            prest = valor / (parc*12)
            porc = sala * 0.3
            porcer = (prest / sala) * 100
            print('Para parcelar uma casa de R${:.2f} em {} anos '.format(valor, parc), end=' ')
            print('a prestação será de R${:.2f}'.format(prest))
            if prest <= porc:
                print('Parcelamento APROVADO!')
                condiçoes = str(input('Quer fazer outro parcelamento? ')).title().strip()
            elif condiçoes:
                print('Parcelamento NEGADO!\n{:.1f}% do salário, LEIA atentamente as condições!'.format(porcer))
                print('==' * 30)
                print('Para o parcelamento ser aprovado\nimediatamente o valor das\nprestações não devem ser superiores\na 30% do valor salarial.')
                print('==' * 30)
                condiçoes = str(input('Quer refazer?')).title().strip()
print('Agradecemos pela preferencia')
        

    
