import datetime


class Product:


    def __init__(self, user, name, curs, dollar_curs, amount, value):
        self.user = user
        self.name = name
        self.curs = curs
        self.dollar_curs = dollar_curs
        self.amount = amount
        self.value = value

    def __str__(self):
        return (f'{datetime.datetime.now()}\t user {self.user}\t{self.name}\t \t amount:\t{self.amount}\t '
                f'rate:\t \t{self.curs}\tfor\t{self.value} \t'
                f'$ price:\t{self.dollar_curs}')

def new_t(nr_tr):
    user = input('Username: ')
    currency = input('Currency: ')
    buying_rate = float(input('Buying rate: '))
    dollar_rate = float(input("Dollar rate: "))
    amount = float(input('Amount: '))
    value = float(input('Value: '))
    nr_tr = Product(user.upper(), currency.upper(), buying_rate.__round__(2), dollar_rate.__round__(2),
                    amount.__round__(6),
                    value.__round__(2))
    buy_list.append(nr_tr)
    return nr_tr

def save_txt():
    file = open(r'C:\Users\Milka\PycharmProjects\UDEMY\Programy\Wallet\wallet.txt', 'a')
    file.write(f'Trade')
    file.write('\n')
    for products in buy_list:
        file.write(f'{products}')
        file.write('\n')
    file.write('\n')
    file.close()
    print('\n')
    print(f'Report was saved. \nCreate {len(buy_list)} new position. ')


buy_list = []


def go():
    a = None
    while a != 'Q':
        try:
            nr_tr = input('Name of trasaction: ')
            new_t(nr_tr)
            print('Saved')
            a = input(" to quit press 'Q:',\n "
                      "to next trade, press nay key.  ")
        except:
            print('Error!  Please try again..')
    save_txt()


go()


