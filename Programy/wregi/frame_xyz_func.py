import frame_ship_info
import datetime
import frame_program_info


def count_x(frame, add):
    base = frame * frame_ship_info.frame_spacing
    x = base + add
    #print(f'X:{x}')
    return x


def count_y(side_value, side):
    if side == "L":
        y = -side_value
    elif side == "R":
        y = side_value
    else:
        y = 0
    #print(f'Y:{y}')
    return y


def count_z(deck, add_high):
    global z
    if deck == 0:
        z = frame_ship_info.bottom + add_high
    if deck == 1:
        z = frame_ship_info.deck_1 + add_high
    if deck == 2:
        z = frame_ship_info.deck_2 + add_high
    if deck == 3:
        z = frame_ship_info.deck_3 + add_high
    if deck == 4:
        z = frame_ship_info.deck_4 + add_high
    #print(f'Z:{z}')
    return z


def count_all_xyz():
    nr = input('Please, Enter name and description of the point: ')
    frame = int(input('Frame: '))
    add = int(input('Add to frame: '))
    side_value = int(input('Side value: '))
    side = input('L/R side: ')
    deck = int(input('Deck: '))
    add_high = int(input('Add high: '))

    print('_________')
    print(f'{nr}\nFrame:{frame}+{add}\nSide:{side}:{side_value}\nDeck:{deck}+{add_high}\n')
    print('_________')
    #print(f'{frame_ship_info.info_about_project}\n{nr}')
    print('_________')
    print(f'''
    X: {count_x(frame, add)}
    Y: {count_y(side_value, side)}
    Z: {count_z(deck, add_high)}
    ''')
    print('_________')
    with open(frame_program_info.path, 'a') as file:
        file.write(f'''
    {datetime.datetime.now()}
    Point nr: {nr}
    ==========================================================
    Frame: {frame}
    Add: {add}
    Side Value: {side_value}
    Side: {side}
    Deck: {deck}
    Add High: {add_high}
    ----------------------------------------------------------
                    TRANSFORM       X: {count_x(frame, add)}
                                    Y: {count_y(side_value, side)}
                                    Z: {count_z(deck, add_high)}
    ----------------------------------------------------------
    ''')
        file.close()
