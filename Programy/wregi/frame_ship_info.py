info_about_project = 'lodołamacz CX56'
frame_spacing = 600

start_frame = -16
end_frame = 36
x_beginning_of_ship = -9600
x_end_of_ship = 39600

bottom = 0
deck_1 = 2400
deck_2 = 5200
deck_3 = 7900
deck_4 = 10000

y_width_of_ship = 17000
y_half_of_width = y_width_of_ship / 2


def show_details():
    print(f'''
    Project name: Kruk CX56
    Type: icebreaker
    Length of the ship: {(abs(x_beginning_of_ship) + x_end_of_ship) / 1000} m
    Width of the ship: {y_width_of_ship / 1000} m
    Decks: 5
        0: {bottom} m
        1: {deck_1 /1000} m
        2: {deck_2 /1000} m
        3: {deck_3 /1000} m
        4: {deck_4 /1000} m
    Frame spacing: {frame_spacing / 1000} m
    ''')
