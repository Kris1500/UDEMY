import definicje

print('Podaj dane pierwszego punktu! ')
a = 't'
while a == 't':
    try:
        definicje.przelicz()
        a = input('Jeśli chesz przekonwertować następny punkt, '
              'wciśnij "t" i ENTER. \nAby zakończyć, wciśnij ENTER.')
    except:
        print('Wprowadzono błędne dane.')
else:
    print('Koniec programu')
