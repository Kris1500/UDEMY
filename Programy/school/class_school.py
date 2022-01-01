class Student:
    def __init__(self, name, group, id, english=None, spanish=None):
        self.name = name
        self.group = group
        self.id = id

        if english is None:
            english = []
        self.english = english

        if spanish is None:
            spanish = []
        self.spanish = spanish

    def __str__(self):
        return (f'Student:\t{self.name}  from group:\t{self.group}  ID:\t{self.id}')

    def add_d_english(self, grade):
        self.english.append(grade)
        print(f'Saved {grade}')

    def add_d_spanish(self, grade):
        self.spanish.append(grade)
        print(f'Saved {grade}')

    def show_english(self):
        print(f'English grades: {self.name}')
        for grades in self.english:
            print(grades)
        try:
            print(f'Average: {(sum(self.english)/len(self.english)).__round__(1)}')
        except ZeroDivisionError:
            print('No grades')

    def show_spanish(self):
        print(f'Spanish grades: {self.name}')
        for grades in self.spanish:
            print(grades)
        try:
            print(f'Average: {(sum(self.spanish) / len(self.spanish)).__round__(1)}')
        except ZeroDivisionError:
            print('No grades')


    def addd(self):
        x = input('What language? ')
        if x == 'english':
            y = int(input('What grade? '))
            if 0 < y < 7:
                self.add_d_english(y)
                self.show_english()
                self.show_spanish()
            else:
                print('Error value')
        if x == 'spanish':
            y = int(input('What grade? '))
            if 0 < y < 7:
                self.add_d_spanish(y)
                self.show_spanish()
                self.show_english()
            else:
                print('Error value')
