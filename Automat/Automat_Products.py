Products = {
    'Mars': {
        'name': 'Mars',
        'price': 3.5,
        'pieces': 20
        },
    'WW': {
        'name': 'WW',
        'price': 3.0,
        'pieces': 20
        },
    'Twix': {
        'name': 'Twix',
        'price': 4.5,
        'pieces': 20
        },
    'KitKat': {
        'name': 'KitKat',
        'price': 3.5,
        'pieces': 20
        },
    'MilkyWay': {
        'name': 'MilkyWay',
        'price': 3.0,
        'pieces': 20
        }
}

def count_pieces(name, buy):
    Products[name]['pieces'] -= buy
    return Products

def print_one_product(name):
    return Products[name]

#print(print_one_product('Twix'))


#print(count_pieces('Twix', 5))
def print_all_products():
    for product in Products:
        print(print_one_product(product))

count_pieces('Mars', 3)
count_pieces('Twix', 2)
count_pieces('WW', 10)
print_all_products()