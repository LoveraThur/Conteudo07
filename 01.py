while True:
    try:
        x = int(input('Insert a number: '))
        y = int(input('Insert other number: '))
    except:
        print('This is not a number')
        print('-'*30)
    else:
        break
if x > y:
    print('Decrescent')
elif y > x:
    print('crescent')
else:
    print('the numbers are equal')
