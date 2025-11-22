km = int(input('Quantos KM\'s rodados: '))
litro = int(input('Qual foi seu consumo DE GASOLINA [ L ]? '))

consumo = km / litro

if consumo >= 0 and consumo <= 4:
    print(f'Consumo de {consumo}')
elif consumo > 4 and consumo <= 8:
    print(f'Consumo de {consumo}')
elif consumo > 8 and consumo <= 10:
    print(f'Consumo de {consumo}')
elif consumo > 10 and consumo <= 12:
    print(f'Consumo de {consumo}')
else:
    print(f'Consumo maior que 12 = {consumo}')