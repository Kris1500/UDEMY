import frame_ship_info

def count_frame(x):
    if x < frame_ship_info.x_end_of_ship and x > frame_ship_info.x_begining_of_ship:
        frame = x // frame_ship_info.frame_spacing
        rest = x % frame_ship_info.frame_spacing
        print(f'Frame {frame}+{rest}mm')
    else:
        print(f'Error! Check X ')

def count_deck(z):
    if z > frame_ship_info.bottom and z < frame_ship_info.deck_1:
        print(f'Bottom, H = {z-0}mm')

    if z >= frame_ship_info.deck_1 and z < frame_ship_info.deck_2:
        print(f'Deck 1 + H = {z - frame_ship_info.deck_1}mm')

    if z >= frame_ship_info.deck_2 and z < frame_ship_info.deck_3:
        print(f'Deck 2 + H = {z - frame_ship_info.deck_2}mm')

    if z >= frame_ship_info.deck_3 and z <= frame_ship_info.deck_4:
        print(f'Deck 3 + H = {z - frame_ship_info.deck_3}mm')

    if z > frame_ship_info.deck_4:
        print(f'Error! Check Z ')

#burta(y) określa usytuowanie względem burt
def count_side(y):
    if y > 0 and y < frame_ship_info.y_width_of_ship/2:
        print(f'{y}mm Right side.')
    if y < 0 and y > frame_ship_info.y_width_of_ship/-2:
        print(f'{abs(y)}mm Left side.')
    if y == 0:
        print(f'in CL')
    if y > frame_ship_info.y_half_of_width:
        print(f'Error! Check Y ')
    if y < -frame_ship_info.y_half_of_width:
        print(f'Error! Check Y ')

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
    count_frame(x)
    count_side(y)
    count_deck(z)
    print('_________')
