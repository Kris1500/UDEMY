import frame_func


a = 't'
while a == 't':
    try:
        frame_func.count_all()
        a = input('If you want to convert the next point, press "t" and ENTER.'
                    'To finish, press ENTER.')
    except:
        print('Check input data!.')
else:
    print('')
    print('Thank you')
