UF = [{'DDD': 61, 'Destino': 'Brasilia'},
      {'DDD': 71, 'Destino': 'Salvador'},
      {'DDD': 11, 'Destino': 'São paulo'},
      {'DDD': 21, 'Destino': 'Rio de Janeiro'},
      {'DDD': 32, 'Destino': 'Juiz de Fora'}, 
      {'DDD': 19, 'Destino': 'Campinas'},
      {'DDD': 27, 'Destino': 'Vitória'},
      {'DDD': 31, 'Destino': 'Belo Horizonte'}
]
while True:
      try:
            number = int(input('Digite o DDD desejado \n>>> '))
      except:
            print('\033[31mDigite um número válido\033[m')
            print('-'*30)
      else:
            break

for e in UF:
      if number in e.values():
            print(f'O DDD {number} é de \033[34m{e['Destino']}\033[m')
            break
else:
      print('\033[31mDDD não cadastrado!\033[m')
