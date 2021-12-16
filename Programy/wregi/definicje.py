import dane_statku
# wregi(x) określa położenie na statku w odniesieniu do wręgów
def wregi(x):
    if x < dane_statku.koniec_statku and x > dane_statku.poczatek_statku:
        wreg = x//dane_statku.rozstaw_wregowy
        reszta = x % dane_statku.rozstaw_wregowy
        print(f'wręg {wreg}+{reszta}mm')
    else:
        print(f'Błąd! Sprawdź X ')

#poklad(z):
def poklad(z):
    if z > dane_statku.dno and z < dane_statku.poklad_1:
        print(f'dno, H = {z-0}mm')

    if z >= dane_statku.poklad_1 and z < dane_statku.poklad_2:
        print(f'pokład 1 + H = {z-dane_statku.poklad_1}mm')

    if z >= dane_statku.poklad_2 and z < dane_statku.poklad_3:
        print(f'pokład 2 + H = {z-dane_statku.poklad_2}mm')

    if z >= dane_statku.poklad_3 and z <= dane_statku.poklad_4:
        print(f'pokład 3 + H = {z-dane_statku.poklad_3}mm')

    if z > dane_statku.poklad_4:
        print(f'Błąd! Sprawdź Z ')

#burta(y) określa usytuowanie względem burt
def burta(y):
    if y > 0 and y < dane_statku.szerokosc_statku/2:
        print(f'{y}mm na prawą burtę.')
    if y < 0 and y > dane_statku.szerokosc_statku/-2:
        print(f'{abs(y)}mm na lewą burtę.')
    if y == 0:
        print(f'w PS')
    if y > dane_statku.polowa_szerokosci:
        print(f'Błąd! Sprawdź Y ')
    if y < -dane_statku.polowa_szerokosci:
        print(f'Błąd! Sprawdź Y ')

def przelicz():
    #try:
    nr = input('Podaj nazwę punktu, lub krótki opis ')
    x = int(input('podaj współrzędna X '))
    y = int(input('podaj współrzędna Y '))
    z = int(input('podaj współrzędna Z '))
    #except:
    #print('Coś poszło nie tak, spróbuj jeszcze raz ')

    print('_________')
    print(f'{nr}\nX:{x}\nY:{y}\nZ:{z}\n')
    print('_________')
    print(f'{dane_statku.informacje_o_projekcie}\n{nr}')
    print('_________')
    wregi(x)
    burta(y)
    poklad(z)
    print('_________')
