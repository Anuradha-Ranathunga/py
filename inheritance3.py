class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
    #graduationyear = 2020
    
    print( f"My graduation year is {self.graduationyear}")
    
  def graduation(self):
      print( f"My graduation year is {self.graduationyear}")
      return 2
  
x = Student("Mike", "Olsen")
#print(x.graduationyear)
print(x.graduation())
print(x.graduationyear)