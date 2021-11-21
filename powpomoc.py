def poleKwadrat():
    a = int(input('Podaj długość boku w cm : '))
    global o
    o=a*a
    print('Pole kwadratu to: ', o, 'cm kw')

#poleKwadrat()
#print(listaPól)
#poleKwadrat()

def poleProstokąt():
    a = int(input('Podaj krótszego długość boku w cm : '))
    b = int(input('Podaj dłuższego długość boku w cm : '))
    o=a*a
    print('Pole prostokąta to: ', o, 'cm kw')
#poleProstokąt()

def poleTrójkąt():
    a = int(input('Podaj długość podstawy w cm : '))
    h = int(input('Podaj wysokość w cm : '))
    o=a/2*h
    print('Pole trójkąta to: ', o, 'cm kw')
#poleTrójkąt()

def poleKoło():
    r = int(input('Podaj promień w cm : '))
    o = 3.14*r*r
    print('Pole koła to: ', o, 'cm kw')
#poleKoło()

