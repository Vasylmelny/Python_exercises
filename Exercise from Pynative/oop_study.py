class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def greeting(self):
        print(f"Hello {self.name} {self.surname}!")

class Student(Person):
    def __init__(self, name, surname, year_of_entry):
        super().__init__(name, surname)
        self.entry = year_of_entry

    def greeting(self, middlename):
        print(f"Hello {self.name} {middlename} {self.surname}!")

    def YearOfStudy(self):
        import datetime
        x = datetime.datetime.now()
        year = x.year
        Study = year - self.entry + 1
        print(Study)

z = Student("John", "Jason",2020)
z.greeting("Young")
z.YearOfStudy()