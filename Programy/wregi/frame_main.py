import frame_func
import frame_xyz_func

a = 't'
while a == 't':
    print('Hello! What type of transformation Do you want?')
    choice = input('[XYZ -> Frame, Deck, Side] - press 1 [Frame, Deck, Side -> XYZ] - press 2')
    if choice.isnumeric():
        choice_checked = int(choice)
        try:
            if choice_checked == 1:
                frame_func.count_all()
            if choice_checked == 2:
                frame_xyz_func.count_all_xyz()
            else:
                print('1 or 2')

        except:
            print('Please, Check input data')

        a = input('If you want to convert the next point, press "t" and ENTER.'
        'To finish, press ENTER.')

    else:
        print('CHOICE 1 or 2')


