import frame_ship_info
import frame_program_info
import datetime


# count_frame(x): - converts the coordinate x into frames.


def count_frame(x):
    if frame_ship_info.x_end_of_ship > x > frame_ship_info.x_beginning_of_ship:
        frame = x // frame_ship_info.frame_spacing
        rest = x % frame_ship_info.frame_spacing
        return f'Frame: {frame} + {rest}'
    else:
        print(f'Error! Check X ')

# count_deck(z): - converts the coordinate z into deck and counting high above this deck.


def count_deck(z):
    if frame_ship_info.bottom < z < frame_ship_info.deck_1:
        return f'Bottom, H = {z-0}mm'
        # return {z-0}

    if frame_ship_info.deck_1 <= z < frame_ship_info.deck_2:
        return f'Deck 1 + H = {z - frame_ship_info.deck_1}mm'
        # return {z - frame_ship_info.deck_1}

    if frame_ship_info.deck_2 <= z < frame_ship_info.deck_3:
        return f'Deck 2 + H = {z - frame_ship_info.deck_2}mm'
        # return {z - frame_ship_info.deck_2}

    if frame_ship_info.deck_3 <= z <= frame_ship_info.deck_4:
        return f'Deck 3 + H = {z - frame_ship_info.deck_3}mm'
        # return {z - frame_ship_info.deck_3}
    if frame_ship_info.bottom > z > frame_ship_info.deck_4:
        return f'Error! Check Z '


# count_side(y): - converts the coordinate y into Left side or Right side and showing the value.


def count_side(y):
    if 0 < y < frame_ship_info.y_width_of_ship/2:
        return f'{y}mm Right side.'
    elif 0 > y > frame_ship_info.y_width_of_ship/-2:
        return f'{abs(y)}mm Left side.'
    elif y == 0:
        return f'in CL'
    elif y > frame_ship_info.y_half_of_width:
        return f'Error! Check Y'
    elif y < -frame_ship_info.y_half_of_width:
        return f'Error! Check Y'

# count_all(): - counting X,Y,Z on FRAME, DECK and SIDE


def count_all():
    nr = input('Please, Enter name and description of the point: ')
    x = int(input('Coordinate X: '))
    y = int(input('Coordinate Y: '))
    z = int(input('Coordinate Z: '))

    print('_________')
    print(f'{nr}\nX:{x}\nY:{y}\nZ:{z}\n')
    print('_________')
    print(f'{frame_ship_info.info_about_project}\n{nr}')
    print('_________')
    print(count_frame(x))
    print(count_side(y))
    print(count_deck(z))
    print('_________')
    with open(frame_program_info.path_2, 'a') as file:
        file.write(f'''
    {datetime.datetime.now()}
    Point nr: {nr}
    ==========================================================
    X: {x}        TRANSFORM    {count_frame(x)}  
    Y: {y}                     {count_side(y)} 
    Z: {z}                     {count_deck(z)} 
    ----------------------------------------------------------
    ----------------------------------------------------------
    ''')
        file.close()
