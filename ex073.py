time=('Santos', 'Atlético-MG', 'Corinthias', 'Cuiabá', 'Internacional', 'Avaí', 'Bragantino', 'Palmeiras', 'Flamengo', 'Critiba', 'São Paulo', 'Botafogo', 'Fluminense', 'America-MG', 'Ceará', 'Athetico-GO', 'Goiás', 'Juventude', 'Fortaleza')
print('-=' * 15)
print('Tabela do Brasileirão: {}'. format(time))
print('-=' * 15)
print('Classificados para libertadores: {}'. format(time[0:4]))
print('-=' * 15)
print('Times no rebaixamento: {}'.format(time[15:]))
print('-=' * 15)
print('Times em ordem alfabetica: {}'.format(sorted(time)))
print('-=' * 15)
print(f'O time do São paulo esta na {time.index("São Paulo")+ 1} posição.')