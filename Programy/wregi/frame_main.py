import frame_func
import frame_xyz_func
import frame_ship_info

a = 't'
while a == 't':
    choice = input('''
    Choose what You want to do?
    
    XYZ -> Frame, Deck, Side - press 1 
    Frame, Deck, Side -> XYZ - press 2
    See project details      - press 3
    ''')
    if choice.isnumeric():
        choice_checked = int(choice)
        try:
            if choice_checked == 1:
                frame_func.count_all()

            elif choice_checked == 2:
                frame_xyz_func.count_all_xyz()

            elif choice_checked == 3:
                frame_ship_info.show_details()

            else:
                print('Choose from 1 to 3')
                continue

        except:
            print('Please, Check input data')
            continue

        a = input('If you want to convert new point, press "t" and ENTER.'
                  'To finish, press ENTER.')

    else:
        print('Choose from 1 to 3')
