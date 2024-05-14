class Person:
    def __init__(self, name):
        self.name = name #public
        self.__age = 25 #private
        self._city = "Panadura" #protected access modifier
   
    def _calculate_age(self): #this one also protected
       return 30
   
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
        
    def _calculate_age(self):
        age = super(Student,self)._calculate_age()
        return age - 5
        
    def print_city(self):
        print(self._city)
        
        
Anuradha = Student("Anuradha")
Anuradha.sleep()
Anuradha.set_age(30)
print(Anuradha._city)

#private varibale pitatha idan access karanna bari unata protected variable pitath idan access karanna puluwan. 

'''
Sleeping... Anuradha
Panadura
'''

'''
Private
prptected
public
'''


