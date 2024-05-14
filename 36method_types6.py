class Person:
    
    types = ['Student' , 'Teacher' ,'Librarian'] 
    def __init__(self,name):
        print("Person is created.")
        self.name= name
        
    def print_name(self):
        print(self)
        print("Name : ", self.name)
        
    @classmethod
    def get_types(cls):
        return cls.types
    
    @staticmethod #object eke thiyena attribute and class eke thiyena attribute access karanna ba. 
    def get_person(person_type):
        print(person_type)
        print('Static method')
    #@Static method=> normal function ekak, speciality eka wenne class ekata kisidu sambandayak nathuwa use karanna puluwan.
        
    
        
Anu = Person("Anu")
Anu.print_name()

Person.print_name(Anu)

print(Person.get_types())
Anu.get_person('Student')

'''
Person is created.
<__main__.Person object at 0x000001EC9BD368A0>
Name :  Anu
<__main__.Person object at 0x000001EC9BD368A0>
Name :  Anu
['Student', 'Teacher', 'Librarian']
Student
Static method
'''