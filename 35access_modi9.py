#varibale ekak child class ekak athule access karanna puluwan wenna hadanna => protected 
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25 #private
        self._city = "Panadura" #protected access modifier
   
   
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
        
    def print_city(self):
        print(self._city)
        
        
Anuradha = Student("Anuradha")
Anuradha.sleep()
Anuradha.set_age(30)
Anuradha.print_city()

'''
Sleeping... Anuradha
Panadura
'''

#protected variable child class ekakadi access karanna puluwan. 