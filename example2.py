class Instructor:

  #def __init__(self, name, address):
   # self.name = name
    #self.address = address
   
    
  def display(self,name, address, subject_name):
        self.name = name
        print(f"Hi, I am {self.name} and I teach {subject_name}")

Instructor_1= Instructor()
#print(Instructor_1.name)
Instructor_1.display("Jenny","Delhi",  "Python")