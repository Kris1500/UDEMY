class User:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_age(self, message):
        print(message, 'wiek to: ', self.age, self.name)


user1=User(25, 'zosia')
user1.print_age('kotrek')