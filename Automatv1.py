import datetime

listaPilosc = [15, 15]
listaPcena = [3, 2]  # zrob slownik
listaPnumer = [1, 2, 9]
listaMonet = [1, 2, 5]
p1 = listaPilosc[0]
p2 = listaPilosc[1]
s = 0  # pomoc
m = []
while True:
    x = int(input('wybierz produkt: \n 1-pepsi \n 2-fanta \n'))
    a = 0
    c = 0
    if x in listaPnumer:
        if x == 1:
            # a=0	# pomoc
            # c=0	#pomoc
            p1Cena = listaPcena[0]  # cena produktu
            while a < p1Cena:  # jesli moneta mniejsza od ceny, wrzuç next
                c = int(input('wrzuc monete: '))
                if c not in listaMonet:
                    print('nieprawidlowa moneta')
                else:
                    a = a + c
                    s += c  # w kasecie
                    m.append(c)
            print(m)
            print('wydaje towar')
            print('wplacono: ', a, 'zl')
            p1 -= 1

            if p1 == 13:
                print('\n RAPORT \n')
                print('Automat przy ilucy Lawendowej 34, Gdansk')
                print(datetime.datetime.now())
                print('pozostalo: \n', 'produkt 1', p1, 'sztuk \n', 'produkt 2', p2, 'sztuk \n')
                print('stan konta to: ', int(s), 'zlotych')
                print('monety: \n \n  1 - ', m.count(1), 'sztuk, \n  2 - ', m.count(2), 'sztuk, \n  5 - ', m.count(5),
                      'sztuk \n')
            else:
                print('ok')

        if x == 2:
            # a=0	# pomoc
            # c=0	#pomoc
            p2Cena = listaPcena[1]  # cena produktu
            while a < p2Cena:  # jesli moneta mniejsza od ceny, wrzuç next
                c = int(input('wrzuc monete: '))
                if c not in listaMonet:
                    print('nieprawidlowa moneta')
                else:
                    a = a + c
                    s += c  # w kasecie
                    m.append(c)
            print(m)
            print('wydaje towar')
            print('wplacono: ', a, 'zl')
            p2 -= 1
            if p2 == 13:
                print('\n RAPORT \n')
                print('-----------------')
                print('Automat przy ulicy Lawendowej 34, Gdansk')
                print(datetime.datetime.now())
                print('pozostalo: \n', 'produkt 1', p1, 'sztuk \n', 'produkt 2', p2, 'sztuk \n')
                print('stan konta to: ', int(s), 'zlotych')
                print('monety: \n \n  1 - ', m.count(1), 'sztuk, \n  2 - ', m.count(2), 'sztuk, \n  5 - ', m.count(5),
                      'sztuk \n')

            else:
                print('pozostalo: ', p2, 'produktu 2, stan konta :', int(s), '\n')
        if x == 9:
            print('raport')
    if x not in listaPnumer:
        print('wybierz nr z listy')
    else:
        print('wybierz produkt z listy')