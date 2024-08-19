class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, firstname, lastname):
    super().__init__(firstname, lastname)

x = Student("Mike", "Olsen")
x.printname()