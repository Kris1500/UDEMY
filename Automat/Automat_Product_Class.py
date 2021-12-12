class Product:

    def __init__(self, name, price, pieces):
        self.name = name
        self.price = price
        self.pieces = pieces
        list_products = []
    def __str__(self):
        return (f'Product: {self.name} cost: {self.price} in machine left: {self.pieces} pieces')


#    def count_pieces(self, Product, piec):
#        self.name = name
#        self.pieces -= piec

#funkcja zmieniajaca cene

#funkcja zmieniajaca nazwe

#funkcja zmieniajaca ilosc



Mars = Product('Mars', 3.5, 20)
WW = Product('WW', 2.5, 20)

print(Mars)
print(Mars.price)