while True:
    try:
        a = int(input('Valor de A: '))
        b = int(input('Valor de B: '))
        c = int(input('Valor de C: '))
        d = int(input('Valor de D: '))
    except:
        print('Valor Inválido!')      
        print('-'*30)
    else:
        break
if b > c and d > a:
    if c + d > a + b:
        print('Valores Aceitos!')
    else:
        print('Valores não aceitos!')
else:
    print('Valores não aceitos!')