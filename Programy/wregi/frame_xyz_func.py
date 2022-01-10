import frame_ship_info


def count_x(frame, add):
    base = frame * frame_ship_info.frame_spacing
    x = base + add
    return x


def count_y(side_value, side):
    if side == "L":
        y = -side_value
    elif side == "R":
        y = side_value
    else:
        y = 0
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
    return z


def count_all_xyz():
    nr = input('Please, Enter name and description of the point: ')
    aframe = int(input('Frame: '))
    aadd = int(input('Add to frame: '))
    aside_value = int(input('Side value: '))
    aside = input('L/R side: ')
    adeck = int(input('Deck: '))
    aadd_high = int(input('Add high: '))

    print('_________')
    print(f'{nr}\nFrame:{aframe}+{aadd}\nSide:{aside}:{aside_value}\nDeck:{adeck}+{aadd_high}\n')
    print('_________')
    #print(f'{frame_ship_info.info_about_project}\n{nr}')
    print('_________')
    print('X:', count_x(aframe, aadd))
    print('Y:', count_y(aside_value, aside))
    print('Z:', count_z(adeck, aadd_high))
    print('_________')



