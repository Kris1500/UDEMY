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
        print(f'Average: {(sum(self.english)/len(self.english)).__round__(1)}')

    def show_spanish(self):
        print(f'Spanish grades: {self.name}')
        for grades in self.spanish:
            print(grades)

# grades should be from 1 to 6!
# min 4 grades to pass
#class # def # main

student_1 = Student('Jan Nowak', '1C', 35)

student_1.add_d_english(5)
student_1.add_d_english(4)
student_1.add_d_english(4)
print(student_1.english)
student_1.show_english()
