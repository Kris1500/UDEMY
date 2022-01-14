import frame_ship_info
import datetime
import frame_program_info


def count_x(frame, add):
    if frame_ship_info.start_frame <= frame <= frame_ship_info.end_frame:
        base = frame * frame_ship_info.frame_spacing
        x = base + add
        return x
    else:
        return f'Frame is out of range'


def count_y(side_value, side):
    if side == "L":
        if -frame_ship_info.y_half_of_width <= side_value < 0:
            y = -side_value
        else:
            return f'Side value is out of range'
    elif side == "R":
        if 0 < side_value <= frame_ship_info.y_half_of_width:
            y = side_value
        else:
            return f'Side value is out of range'
    elif side == "CL":
        y = 0

    else:
        y = 0
    return y


def count_z(deck, add_high):
    if deck == 0:
        z = frame_ship_info.bottom + add_high
    elif deck == 1:
        z = frame_ship_info.deck_1 + add_high
    elif deck == 2:
        z = frame_ship_info.deck_2 + add_high
    elif deck == 3:
        z = frame_ship_info.deck_3 + add_high
    elif deck == 4:
        z = frame_ship_info.deck_4 + add_high
    else:
        return f'Deck value is out of range'
    return z


def count_all_xyz():
    nr = input('Please, Enter name and description of the point: ')
    frame = int(input('Frame: '))
    add = int(input('Add to frame: '))
    side_value = int(input('Side value: '))
    side = input('L/CL/R side: ')
    deck = int(input('Deck: '))
    add_high = int(input('Add high: '))

    print('_________')
    print(f'{nr}\nFrame:{frame}+{add}\nSide:{side}:{side_value}\nDeck:{deck}+{add_high}\n')
    print('_________')
    print('_________')
    print(f'''
    X: {count_x(frame, add)}
    Y: {count_y(side_value, side)}
    Z: {count_z(deck, add_high)}
    ''')
    print('_________')
    with open(frame_program_info.path_2, 'a') as file:
        file.write(f'''
    {datetime.datetime.now()}
    Point nr: {nr}
    ==========================================================
    Frame: {frame}      TRANSFORM       X: {count_x(frame, add)}
    Add: {add}                          Y: {count_y(side_value, side)}    
    Side Value: {side_value}            Z: {count_z(deck, add_high)}
    Side: {side}
    Deck: {deck}                        
    Add High: {add_high}
    ----------------------------------------------------------
    ----------------------------------------------------------
    ''')
        file.close()
