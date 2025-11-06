par = 0
impar = 0
negativo = 0
positivo = 0
for i in range(0,5):
    while True:
        try:
            n = int(input(f'Digite o {i+1}º numero: '))
        except:
            print('\033[31mNúmero inválido\033[m')    
            print('-'*30)
        else:
            break
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

    if n >= 0:
        positivo += 1
    else:
        negativo += 1
        print('-'*30)
print(f'Tivemos {par} numeros pares \nTivemos {impar} numeros impares \nTivemos {negativo} numeros negativos \nTivemos {positivo} numeros positivos')