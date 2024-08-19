class Person:
  def __init__(self, fname, lname, year1):
    self.firstname = fname
    self.lastname = lname
    self.yearr = year1

  def printname(self):
    print(self.firstname, self.lastname, self.yearr)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname , year)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
x.printname()