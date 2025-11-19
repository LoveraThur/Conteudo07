while True:
    try:
        number = float(input('Insert a number\n>>> '))
    except:
        print('\033[31mThis is NOT a Number\033[m')
        print('-'*30)
    else:
        print('-'*30)
        if number > 0 and number <= 25:
            print('Range [0,25]')
        elif number > 25 and number <= 50:
            print('range [25, 50]')
        elif number > 50 and number <= 75:
            print('Range [50, 75]')
        elif number > 75 and number <= 100:
            print('Range [75, 100]')
        else:
            print('Out of Range')
        break