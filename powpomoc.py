def squareArea():
    a = int(input('Podaj długość boku w cm : '))
    global o
    o=a*a
    print('Pole kwadratu to: ', o, 'cm kw')


def rectangleArea():
    a = int(input('Podaj krótszego długość boku w cm : '))
    b = int(input('Podaj dłuższego długość boku w cm : '))
    o=a*a
    print('Pole prostokąta to: ', o, 'cm kw')


def squareTriangle():
    a = int(input('Podaj długość podstawy w cm : '))
    h = int(input('Podaj wysokość w cm : '))
    o=a/2*h
    print('Pole trójkąta to: ', o, 'cm kw')
)

def squareCircle():
    r = int(input('Podaj promień w cm : '))
    o = 3.14*r*r
    print('Pole koła to: ', o, 'cm kw')


