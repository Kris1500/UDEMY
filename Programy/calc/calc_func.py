def square_area():
    a = int(input('Podaj długość boku w cm : '))
    o = a * a
    print('Pole kwadratu to: ', o, 'cm kw')


def rectangle_area():
    a = int(input('Podaj krótszego długość boku w cm : '))
    b = int(input('Podaj dłuższego długość boku w cm : '))
    o = a * b
    print('Pole prostokąta to: ', o, 'cm kw')


def square_triangle():
    a = int(input('Podaj długość podstawy w cm : '))
    h = int(input('Podaj wysokość w cm : '))
    o = a / 2 * h
    print('Pole trójkąta to: ', o, 'cm kw')


def square_circle():
    r = int(input('Podaj promień w cm : '))
    o = 3.14 * r * r
    print('Pole koła to: ', o, 'cm kw')

