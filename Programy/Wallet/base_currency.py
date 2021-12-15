import datetime

'''
Zapisuje transakcje kupna kryptowalut do pliku txt.'''


class Product:

    def __init__(self, user, name, curs, dolar_curs, amount, value):
        self.user = user
        self.name = name
        self.curs = curs
        self.dolar_curs = dolar_curs
        self.amount = amount
        self.value = value

    def __str__(self):
        return (f'{datetime.datetime.now()}\t user {self.user}\t{self.name}\t \t ilosć:\t{self.amount}\t '
                f'kurs trans:\t \t{self.curs}\tza\t{self.value} \t'
                f'dolara-kurs:\t{self.dolar_curs}')


def new_t(nr_tr):
    user = input('Podaj użytkownika: ')
    name = input('Podaj nazwę kupowanej waluty: ')
    curs = float(input('Podaj kurs kupna: '))
    dolar_curs = float(input("Podaj kurs dolara: "))
    amount = float(input('Podaj ilosc waluty: '))
    value = float(input('Podaj wartosc: '))
    nr_tr = Product(user.upper(), name.upper(), curs.__round__(2), dolar_curs.__round__(2), amount.__round__(6),
                    value.__round__(2))
    buy_list.append(nr_tr)
    return nr_tr


def save_txt():
    file = open(r'C:\Users\Milka\PycharmProjects\UDEMY\Programy\Wallet\wallet.txt', 'a')
    file.write(f'Z A K U P Y')
    file.write('\n')
    for products in buy_list:
        file.write(f'{products}')
        file.write('\n')
    file.write('\n')
    file.close()


buy_list = []


def go():
    a = None
    while a != 'Q':
        try:
            nr_tr = input('Podaj nazwę transakcji: ')
            new_t(nr_tr)
            print('zapisano!')
            a = input(" Jeżeli chcesz zakończyć, wybierz 'Q:' i wciśnij enter,\n "
                      "aby wprowadzić następną pozycję wciśnij dowolny klawisz i enter  ")
        except:
            print('UPS...  coś poszło nie tak!  Spróbuj ponownie..')
    save_txt()


go()

print('\n')
print(f' Dziękuję! Życzę miłego dnia :) Raport został dopisany do pliku txt. \n Utworzono {len(buy_list)} pozycji. ')
