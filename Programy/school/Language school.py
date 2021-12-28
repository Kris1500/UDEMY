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
        return (f'Uczeń {self.name} z grupy {self.group} o id:{self.id}')

    def add_d_english(self, a):
        self.english.append(a)
        print(f'Dodano ocenę {a}')

    def add_d_spanish(self, a):
        self.spanish.append(a)
        print(f'Dodano ocenę {a}')

    def show_english(self):
        print(f'Oceny z angielskiego: {self.name}')
        for i in self.english:
            print(i)

    def show_spanish(self):
        print(f'Oceny z hiszpańskiego: {self.name}')
        for i in self.spanish:
            print(i)


student_1 = Student('Jan Kowal', '1C', 35)

student_1.add_d_english(5)
student_1.add_d_english(4)
print(student_1.english)
student_1.show_english()
