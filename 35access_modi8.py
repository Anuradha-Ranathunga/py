#parent class
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25 
   
   
    def set_age(self,age):
        self.__age = age
     
    def get_age(self):
        return self.__age
        
    def sleep(self):
        print("Sleeping...", self.name)

#child class       
class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)
        
    def print_age(self):
        print(self.__age)
        
        
Anuradha = Student("Anuradha")
Anuradha.sleep()
Anuradha.set_age(30)
Anuradha.print_age()

'''
Sleeping... Anuradha
Traceback (most recent call last):
  File "c:\Users\Anuradha\Desktop\Python\35access_modi8.py", line 29, in <module>
    Anuradha.print_age()
  File "c:\Users\Anuradha\Desktop\Python\35access_modi8.py", line 23, in print_age
    print(self.__age)
          ^^^^^^^^^^
AttributeError: 'Student' object has no attribute '_Student__age'
'''

#private variable subclass ekakin wath access karanna ba